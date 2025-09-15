# 1. Import modules
import requests          # To talk to websites (send HTTP requests)
from bs4 import BeautifulSoup  # To parse HTML and extract text
import csv               # To save results in CSV files

# 2. Ask for URL
url = input("Paste the website URL to scrape: ")

# 3. Send request
response = requests.get(url)
html_content = response.text

# 4. Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 5. Automatically pick main text tags
text_tags = ['p', 'h1', 'h2', 'h3']  # paragraphs and headers
elements = []

for tag in text_tags:
    elements.extend(soup.find_all(tag))  # find all tags and add to list

# 6. Clean text
elements_text = [el.get_text().strip() for el in elements if el.get_text().strip() != ""]

# 7. Save to CSV (append mode)
with open("scraped_data.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for text in elements_text:
        writer.writerow([text])

# 8. Print results
for text in elements_text:
    print(text)
