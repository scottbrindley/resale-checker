from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

url = "https://darkmofo.net.au/resales"

with sync_playwright() as p:
    # Launch a headless browser
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Navigate to the page and wait until all network activity stops
    page.goto(url, wait_until="networkidle")
    
    # Grab the completed HTML after JS has run
    rendered_html = page.content()
    browser.close()

# Extract ticket resales from web page using BeautifulSoup
soup = BeautifulSoup(rendered_html, 'html.parser')
program_links = soup.find_all("a", href=re.compile(r"^/program/"))

# Extract and clean the text from each tag
for link in program_links:
    print(link.get_text(strip=True))

