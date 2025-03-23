import requests
import sqlite3
import time
from bs4 import BeautifulSoup

# URL of the fake job listings
URL = "https://realpython.github.io/fake-jobs"

# Headers to simulate a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def get_page_content(url, retries=3, delay=2):
    """Fetch page content with retries and error handling."""
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()  # Raise HTTP errors if any
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)  # Wait before retrying
    print("Failed to retrieve page after multiple attempts.")
    return None


def scrape_jobs():
    """Scrape job listings from the webpage."""
    html_content = get_page_content(URL)
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, "html.parser")
    jobs = []

    job_cards = soup.find_all("div", class_="card-content")
    for job_card in job_cards:
        title = job_card.find("h2", class_="title").text.strip()
        company = job_card.find("h3", class_="company").text.strip()
        location = job_card.find("p", class_="location").text.strip()
        description = job_card.find("div", class_="description").text.strip()
        application_link = job_card.find("a")["href"]

        jobs.append((title, company, location, description, application_link))

    return jobs


def setup_database():
    """Create SQLite database and jobs table if not exists."""
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            application_link TEXT,
            UNIQUE(title, company, location)
        )
    """)
    conn.commit()
    conn.close()


def save_jobs_to_db(jobs):
    """Save new job listings to the database, avoiding duplicates."""
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()

    for job in jobs:
        title, company, location, description, application_link = job
        cursor.execute("""
            INSERT OR IGNORE INTO jobs (title, company, location, description, application_link)
            VALUES (?, ?, ?, ?, ?)
        """, (title, company, location, description, application_link))

    conn.commit()
    conn.close()


def main():
    setup_database()
    jobs = scrape_jobs()

    if jobs:
        save_jobs_to_db(jobs)
        print(f"Saved {len(jobs)} new job listings.")
    else:
        print("No jobs found.")


if __name__ == "__main__":
    main()
