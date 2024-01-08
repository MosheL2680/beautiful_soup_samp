import requests
from bs4 import BeautifulSoup

def count_divs(url):
    try:
        # Fetch the HTML content of the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad requests

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Count the number of HTML div tags
        div_count = len(soup.find_all('div'))

        return div_count

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

if __name__ == "__main__":
    website_url = "https://www.one.co.il/"
    div_count = count_divs(website_url)

    if div_count is not None:
        print(f"The number of divs on {website_url} is: {div_count}")
