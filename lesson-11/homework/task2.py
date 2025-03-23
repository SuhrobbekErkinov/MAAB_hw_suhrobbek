import sqlite3


def create_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    data = [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]
    cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", data)

    conn.commit()
    conn.close()


def update_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Books SET Year_Published = ? WHERE Title = ?", (1950, "1984"))

    conn.commit()
    conn.close()


def query_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = ?", ("Dystopian",))
    results = cursor.fetchall()

    conn.close()
    return results


def delete_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Books WHERE Year_Published < ?", (1950,))

    conn.commit()
    conn.close()


def add_rating_column():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

    rating_data = [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ]

    for rating, title in rating_data:
        cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))

    conn.commit()
    conn.close()


def advanced_query():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    results = cursor.fetchall()

    conn.close()
    return results


def main():
    create_database()
    insert_data()
    update_data()
    print("Query Result:", query_data())
    delete_data()
    add_rating_column()
    print("Sorted Books:", advanced_query())


if __name__ == "__main__":
    main()
