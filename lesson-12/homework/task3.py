import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    """Initialize and return a headless Chrome WebDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def scrape_laptops(driver):
    """Scrape laptop data from Demoblaze and return a list of dictionaries."""
    URL = "https://www.demoblaze.com/"
    driver.get(URL)
    time.sleep(2)  # Allow page to load

    # Click on the "Laptops" section
    laptops_section = driver.find_element(By.LINK_TEXT, "Laptops")
    laptops_section.click()
    time.sleep(3)  # Wait for laptops to load

    laptop_data = []

    while True:
        products = driver.find_elements(By.CLASS_NAME, "card-block")

        for product in products:
            name = product.find_element(By.CLASS_NAME, "card-title").text.strip()
            price = product.find_element(By.CLASS_NAME, "card-price").text.strip()
            description = product.find_element(By.CLASS_NAME, "card-text").text.strip()

            laptop_data.append({
                "name": name,
                "price": price,
                "description": description
            })

        # Check if "Next" button is available and enabled
        try:
            next_button = driver.find_element(By.ID, "next2")
            if "disabled" in next_button.get_attribute("class"):  # Stop if disabled
                break
            next_button.click()
            time.sleep(3)  # Wait for the next page to load
        except:
            break  # No "Next" button found, end scraping

    return laptop_data


def save_to_json(data, filename="laptops.json"):
    """Save scraped data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Scraped {len(data)} laptops. Data saved to {filename}")


def main():
    """Main function to run the scraping process."""
    driver = setup_driver()

    try:
        laptop_data = scrape_laptops(driver)
        save_to_json(laptop_data)
    finally:
        driver.quit()  # Ensure the browser is closed


if __name__ == "__main__":
    main()
