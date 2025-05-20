import requests  # Importing the requests library to handle HTTP requests
from bs4 import BeautifulSoup  # Importing BeautifulSoup from bs4 to parse HTML content

def get_text_form_url(url):
    # Sending an HTTP GET request to the provided URL
    response = requests.get(url)

    # Checking if the request was successful (status code 200 means OK)
    if response.status_code == 200:

        # Parsing the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the main title of the article (usually an <h1> tag with a specific class)
        title = soup.find('h1', class_='entry-title').get_text(strip=True)

        # Finding all headings (h1 tags with class 'wp-block-heading') and getting their text
        headings = soup.find_all('h1', class_='wp-block-heading')
        headings_text = "\n".join(h.get_text(strip=True) for h in headings)

        # Finding all paragraph tags (<p>) and getting their text
        paragraphs = soup.find_all('p')
        article_text = "\n".join(p.get_text(strip=True) for p in paragraphs)

        # Extracting text from the first unordered list (<ul>) found in the HTML
        list_text_ul = soup.find('ul').get_text(strip=True)

        # Combining all the extracted text into a single string
        all_text = title + article_text + headings_text + list_text_ul
        
        # Returning the combined text
        return all_text

    else:
        # If the request failed, print an error message with the status code
        print(f"failed to get the webpage. Status Code: {response.status_code}")
