import requests
from bs4 import BeautifulSoup
import json

# Step 1: Ask user for URL
url = input("Paste the website URL to scrape: ")

# Step 2: Fetch the page
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Traverse page in order
body = soup.body
scraped_data = []

for element in body.find_all(recursive=True): # type: ignore
    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        scraped_data.append({
            "type": "heading",
            "text": element.get_text(strip=True),
            "children": []
        })
    elif element.name == 'p':
        paragraph = {
            "type": "paragraph",
            "text": element.get_text(strip=True),
            "links": []
        }
        links = element.find_all('a') # type: ignore
        for link in links:
            paragraph["links"].append(link.get('href'))

        if scraped_data and scraped_data[-1]["type"] == "heading":
            scraped_data[-1]["children"].append(paragraph)
        else:
            scraped_data.append(paragraph)

# Step 4: Save structured data to JSON
output_file = "scraped_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, ensure_ascii=False, indent=4)

print(f"✅ Structured data saved to {output_file}")
