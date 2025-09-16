# Level 3: Smart Static Web Scraper

import requests                # talk to websites
from bs4 import BeautifulSoup  # clean and parse HTML
import csv                      # save tables
import json                     # save structured data

# 1️⃣ Ask user for URL
url = input("Paste the website URL to scrape: ")

# 2️⃣ Fetch HTML content
response = requests.get(url)
html_content = response.text

# 3️⃣ Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# 4️⃣ Extract data
paragraphs = [p.get_text().strip() for p in soup.find_all("p") if p.get_text().strip()]
headings = [h.get_text().strip() for h in soup.find_all(["h1", "h2", "h3"]) if h.get_text().strip()]
links = [a["href"] for a in soup.find_all("a", href=True)]

# 5️⃣ Save to CSV (append mode)
with open("scraped_data.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for para in paragraphs:
        writer.writerow(["Paragraph", para])
    for head in headings:
        writer.writerow(["Heading", head])
    for link in links:
        writer.writerow(["Link", link])

# 6️⃣ Save to JSON (overwrite mode)
data = {
    "paragraphs": paragraphs,
    "headings": headings,
    "links": links
}

with open("scraped_data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# 7️⃣ Print summary
print(f"Scraped {len(paragraphs)} paragraphs, {len(headings)} headings, {len(links)} links.")
print("Data saved to scraped_data.csv and scraped_data.json ✅")
