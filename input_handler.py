import re
import requests
from bs4 import BeautifulSoup


def is_url(text):
    return re.match(r'https?://', text.strip()) is not None


def fetch_website_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts & style
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator="\n")
        return text.strip()

    except Exception as e:
        return f"[ERROR FETCHING WEBSITE] {str(e)}"


def process_input(user_input):
    user_input = user_input.strip()

    if is_url(user_input):

        # If LinkedIn URL
        if "linkedin.com" in user_input:
            return """
[LinkedIn URL detected]

For privacy and compliance reasons, please paste the publicly available profile text instead of a LinkedIn URL.
"""

        # Otherwise treat as public website
        return fetch_website_text(user_input)

    else:
        # Normal raw profile text
        return user_input
