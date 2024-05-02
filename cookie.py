import urllib.request
import ssl
from bs4 import BeautifulSoup

def fetch_github_db(url):
    """
    Scrape the textarea content from the github link and return the data in a list
    """
    pass

def get_random_content(contents):
    """
    Return a random element from the given list 
    """
    pass

def generate_cookie_id():
    """
    Generate unique id for a cookie
    """
    pass

def show_features():
    """
    Print existing and new features
    """
    pass

def show_help():
    """
    Display available commands and tutorials
    """
    pass

def exit_app():
    """
    Terminate the app
    """
    pass

def save_cookies(cookies):
    """
    Save the chosen or all cookies 
    """
    pass


def main():
    # greet users

    # fetch quotes and words 

    # track cookie ids and contents  

    # ask for user name and email


    # if users want to see features 

    # if users want to see command list

    # if users want to save cookies

    # if users choose to exit

    pass


# Fetch all quotes
url_quote = "https://github.com/aussieW/skill-confucius-say/blob/master/dialog/en-us/sayings.dialog"

context = ssl._create_unverified_context()
with urllib.request.urlopen(url_quote, context=context) as response_quote:
    quotes = response_quote.read().decode()
    # print(quotes)
    soup = BeautifulSoup(quotes, "html.parser")
    targets = soup.findAll("div", {"class": "react-file-line"})
    if targets:
        for target in targets:
            target_text = target.get_text()
            print(target_text)

context2 = ssl._create_unverified_context()
url_word = "https://github.com/bitdreamer/ZWFlashCards/blob/master/wordlists/zz_all.txt"
with urllib.request.urlopen(url_word, context=context2) as response_word:
    words = response_word.read().decode()
    # print(words)
    soup = BeautifulSoup(words, "html.parser")
    targets_w = soup.findAll("div", {"class": "react-file-line"})
    if targets_w:
        for target in targets_w:
            target_text2 = target.get_text()
            print(target_text2)
