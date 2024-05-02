import urllib.request
import ssl
from bs4 import BeautifulSoup

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
