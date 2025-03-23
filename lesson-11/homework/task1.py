import sqlite3


def create_database():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    """)

    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    data = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]

    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

    conn.commit()
    conn.close()


def update_data():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))

    conn.commit()
    conn.close()


def query_data():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = ?", ("Bajoran",))
    results = cursor.fetchall()

    conn.close()
    return results


def delete_data():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Roster WHERE Age > ?", (100,))

    conn.commit()
    conn.close()


def add_rank_column():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

    rank_data = [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ]

    for rank, name in rank_data:
        cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))

    conn.commit()
    conn.close()


def advanced_query():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    results = cursor.fetchall()

    conn.close()
    return results


def main():
    create_database()
    insert_data()
    update_data()
    print("Query Result:", query_data())
    delete_data()
    add_rank_column()
    print("Sorted Roster:", advanced_query())


if __name__ == "__main__":
    main()
