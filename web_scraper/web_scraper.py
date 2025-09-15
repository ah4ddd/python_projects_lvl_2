# Step 1: Import necessary modules
import requests       # to fetch HTML from websites
from bs4 import BeautifulSoup  # to parse HTML and extract content
import csv            # to save data in CSV format

# Step 2: Ask user for input
url = input("Paste the website URL to scrape: ")               # website link
tag = input("Enter HTML tag to scrape (e.g., 'p', 'div', 'span'): ")  # HTML tag
class_name = input("Enter class name (or leave empty if none): ")      # optional class

# Step 3: Fetch the website content
response = requests.get(url)  # send HTTP GET request to website
if response.status_code == 200:  # check if request was successful
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')  # parse HTML
else:
    print("Failed to retrieve website. Status code:", response.status_code)
    exit()  # stop program if website cannot be loaded

# Step 4: Find all elements with the specified tag and optional class
if class_name:
    elements = soup.find_all(tag, class_=class_name)  # filter by class
else:
    elements = soup.find_all(tag)  # get all tags if class not specified

# Step 5: Extract text from elements
data = []  # list to store text
for element in elements:
    text = element.get_text().strip()  # remove HTML tags and extra spaces
    if text:  # skip empty text
        data.append(text)

# Step 6: Save the scraped data to CSV (append mode)
filename = "scraped_data.csv"  # file name
with open(filename, "a", newline="", encoding="utf-8") as file: #open or create file
    writer = csv.writer(file)
    for row in data:
        writer.writerow([row])  # save each text in a new row

# Step 7: Print scraped data in terminal
print("\nScraped content:")
for row in data:
    print(row)
