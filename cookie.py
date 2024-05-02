import urllib.request
import ssl
from bs4 import BeautifulSoup


def fetch_github_db(url):
    """
    Scrape the textarea content from a github link and return the data in a list
    """
    result = []
    context = ssl._create_unverified_context()

    with urllib.request.urlopen(url, context=context) as response:
        db = response.read().decode()
        # print(quotes)
        soup = BeautifulSoup(db, "html.parser")
        texts = soup.findAll("div", {"class": "react-file-line"})
        if texts:
            for item in texts:
                target_text = item.get_text()
                result.append(target_text)
    return result


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
    # fetch quotes and words
    url_quote = "https://github.com/aussieW/skill-confucius-say/blob/master/dialog/en-us/sayings.dialog"
    quotes, words = [], []
    while len(quotes) == 0:
        quotes = fetch_github_db(url_quote)
    url_word = "https://github.com/bitdreamer/ZWFlashCards/blob/master/wordlists/zz_all.txt"
    while len(words) == 0:
        words = fetch_github_db(url_word)
    print(quotes, words)

    # greet users

    # track cookie ids and contents
    cookies = []

    # ask for username and email

    # if users want to see features

    # if users want to see command list

    # if users want to save cookies

    # if users choose to exit

    pass


# context = ssl._create_unverified_context()
# with urllib.request.urlopen(url_quote, context=context) as response_quote:
#     quotes = response_quote.read().decode()
#     # print(quotes)
#     soup = BeautifulSoup(quotes, "html.parser")
#     targets = soup.findAll("div", {"class": "react-file-line"})
#     if targets:
#         for target in targets:
#             # print(target)
#             target_text = target.get_text()
#             print(target_text)
#
# context2 = ssl._create_unverified_context()
#
# with urllib.request.urlopen(url_word, context=context2) as response_word:
#     words = response_word.read().decode()
#     # print(words)
#     soup2 = BeautifulSoup(words, "html.parser")
#     targets_w = soup2.findAll("div", {"class": "react-file-line"})
#     if targets_w:
#         for target_w in targets_w:
#             target_text2 = target_w.get_text()
#             print(target_text2)


if __name__ == '__main__':
    main()
