import urllib.request
import ssl
from bs4 import BeautifulSoup
from random import *
import re

def fetch_github_db(url):
    """
    Scrape the textarea content from a github link and return the data in a list
    """
    result = []
    context = ssl._create_unverified_context()

    with urllib.request.urlopen(url, context=context) as response:
        db = response.read().decode()
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
    random_range = len(contents)
    random_number = randrange(1, random_range)
    return contents[random_number]


def generate_lotto():
    """
    Generate a list of 6 random numbers between 1-45
    """
    lotto = []
    for _ in range(6):
        lotto.append(randrange(1, 45))
    return lotto

def generate_powerball():
    """
    Generate a random number between 1 and 45
    """
    return randrange(1, 45)

class Cookie:
    def __init__(self):
        self._cookie = {
            'cookie id': 0,
            'quote': '',
            'lotto': [],
            'powerball': 0,
            'chinese': ''
        }

    def get_cookie_dict(self):
        return self._cookie

    def make_full_cookie(self, id, quotes, words):
        self._cookie['cookie id'] = id
        self._cookie['quote'] = get_random_content(quotes)
        self._cookie['lotto'] = generate_lotto()
        self._cookie['powerball'] = generate_powerball()
        self._cookie['chinese'] = get_random_content(words)
        return self.get_cookie_dict()

    def customize_cookie(self, id, quotes, words, option):
        self._cookie['cookie id'] = id
        if option == "quote":
            self._cookie['quote'] = get_random_content(quotes)
        elif option == "lotto":
            self._cookie['lotto'] = generate_lotto()
        elif option == "powerball":
            self._cookie['powerball'] = generate_powerball()
        elif option == "chinese":
            self._cookie['chinese'] = get_random_content(words)
        else:
            print("Oops, this is not in our menu.")
        return self.get_cookie_dict()

    def show_cookie(self):
        cookie_dict = self.get_cookie_dict()
        print()
        print('********FORTUNE COOKIE********')
        for key, value in cookie_dict.items():
            if value not in ['', 0, []]:
                print(f'Your lucky {key}:', value)
        print('********FORTUNE COOKIE********')
        print()

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
    print('Welcome to Fortune Cookie Maker!\n'
          'Open a cookie with a Confucius quote, lotto numbers, powerball number, and a Chinese word.\n'
          'Or customize your cookie with any of the above options.\n'
          'Grab as many fortune cookies as you want.\n'
          'Your cookies can be saved locally or shipped via email if you wish.\n'
          'We will never sell your data. Your email will only be used to ship cookies.\n'
          'Here are the steps: \n'
          '1. (Optional) Fill out name and email if you want to get the cookies in your inbox. \n'
          '2. Follow the prompt to enter a command.\n'
          '3. Repeat step 2 or save cookies or exit.\n')
    print('A fresh batch is in the oven. One moment...\n')

    # fetch quotes and words
    url_quote = "https://github.com/wukongO-O/361-s24/blob/main/db-quotes.txt"
    quotes, words = [], []
    while len(quotes) == 0:
        quotes = fetch_github_db(url_quote)
    url_word = "https://github.com/wukongO-O/361-s24/blob/main/db-words.txt"
    while len(words) == 0:
        words = fetch_github_db(url_word)
    # print(quotes, words)

    # track cookie contents, user information
    cookies = []
    user = {
        'name': '',
        'email': ''
    }

    # ask for username and email
    print("If you'd like to email the cookies later, tell us your name and email address following the prompts.\n"
          "Otherwise, press return to continue.\n")
    username = input("Your name: ")
    email_add = input("Your email: ")
    user['name'] = username
    user['email'] = email_add

    while True:
        current_command = input("Type 'cookie' to get a new fortune cookie,\n "
                                "'quote' to get a cookie with quote only, \n"
                                "'lotto' to get a cookie with lottery numbers only, \n "
                                "'power' to get a cookie with a power ball number only, \n"
                                "'chinese' to get a cookie with Chinese word only, \n"
                                "or 'help' to see the full list of commands: \n")
        new_cookie = Cookie()
        new_cookie_id = len(cookies) + 1

        # when user enters a non-cookie related command
        if current_command.lower() == "feature":
            show_features()
            continue
        elif current_command.lower() == "help":
            show_help()
            continue
        elif current_command.lower() == "save.*":
            save_cookies()
            continue
        elif current_command.lower() == "exit":
            break

        # when user enters a cookie-related command
        if current_command.lower() == "cookie":
            new_cookie.make_full_cookie(new_cookie_id, quotes, words)
        elif current_command.lower() == "quote":
            new_cookie.customize_cookie(new_cookie_id, quotes, words, "quote")
        elif current_command.lower() == "lotto":
            new_cookie.customize_cookie(new_cookie_id, quotes, words, "lotto")
        elif current_command.lower() == "power":
            new_cookie.customize_cookie(new_cookie_id, quotes, words, "powerball")
        elif current_command.lower() == "chinese":
            new_cookie.customize_cookie(new_cookie_id, quotes, words, "chinese")
        else:
            print("Oops, this is not in our menu \n")
            continue

        cookies.append(new_cookie)
        new_cookie.show_cookie()


if __name__ == '__main__':
    main()
