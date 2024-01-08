import requests
from bs4 import BeautifulSoup

def count_word_occurrences(url, target_word):
    try:
        # Fetch the HTML content of the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad requests

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Count the occurrences of the target word
        word_count = soup.text.lower().count(target_word.lower())

        return word_count

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

if __name__ == "__main__":
    website_url = "https://www.one.co.il/"  # Change this to the desired website URL
    target_word = "כדור"  # Change this to the desired word

    word_count = count_word_occurrences(website_url, target_word)

    if word_count is not None:
        print(f"The word '{target_word}' appears {word_count} times on {website_url}")
