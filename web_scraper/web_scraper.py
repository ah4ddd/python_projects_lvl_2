import requests
from bs4 import BeautifulSoup
import csv
import json

url = input("Paste the website URL to scrape: ")

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

paragraphs = [p.get_text().strip() for p in soup.find_all("p") if p.get_text().strip()]
headings = [h.get_text().strip() for h in soup.find_all(["h1", "h2", "h3"]) if h.get_text().strip()]
links = [a["href"] for a in soup.find_all("a", href=True)]

with open("scraped_data.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for para in paragraphs:
        writer.writerow(["Paragraph", para])
    for head in headings:
        writer.writerow(["Heading", head])
    for link in links:
        writer.writerow(["Link", link])

data = {
    "paragraphs": paragraphs,
    "headings": headings,
    "links": links
}
with open("scraped_data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print(f"Scraped {len(paragraphs)} paragraphs, {len(headings)} headings, {len(links)} links.")
print("Data saved to scraped_data.csv and scraped_data.json ✅")
