import requests
from bs4 import BeautifulSoup

def scrape_links(links):
    print("[web_scraper] Scraping web pages...")
    contents = []

    for url in links:
        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")
            text = soup.get_text(separator=" ", strip=True)
            if len(text) > 100:
                contents.append({"url": url, "text": text})
        except Exception as e:
            print(f"[web_scraper] Failed to scrape {url}: {e}")
            continue

    return contents