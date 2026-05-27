from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

def check_resales():

    url = "https://darkmofo.net.au/resales"
    resale_events = []

    print(f"Checking for ticket resales at {url}...")

    with sync_playwright() as p:
        # Launch a headless browser
        browser = p.chromium.launch(headless=True, args=["--disable-dev-shm-usage"])
        page = browser.new_page()
        
        # Wait for content containing resales to load
        page.goto(url)
        page.wait_for_selector("a[href^='/program/']", timeout=10000)
        
        # Grab the completed HTML after JS has run
        rendered_html = page.content()
        browser.close()

    # Extract ticket resales from web page using BeautifulSoup
    soup = BeautifulSoup(rendered_html, 'html.parser')
    program_links = soup.find_all("a", href=re.compile(r"^/program/"))

    # Extract and clean the text from each tag
    print("Tickets available for resale at the following events:")
    for link in program_links:
        event = link.get_text(strip=True)
        print(event)
        resale_events.append(event)

    return resale_events

if __name__ == "__main__":
    check_resales()
        

    

