import requests
from bs4 import BeautifulSoup
import csv

url = input("Paste the website URL to scrape: ")
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

all_quotes = []  # empty list to store results

for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    all_quotes.append([text, author])

with open("quotes.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])  # header
    writer.writerows(all_quotes)

for quote, author in all_quotes:
    print(f"{quote} — {author}")

