import os
import urllib.request
import ssl
from bs4 import BeautifulSoup
from random import *
import re
import json
# For microservice A - email sender
from dotenv import load_dotenv
import requests
import os


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


def fetch_text_file_db(file_path):
    """
    Get content as a list from a text file
    :param file_path: relative file path
    :return: a list of lines from the text file
    """
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            result.append(line.strip())
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

    def get_cookie_content(self):
        """
        Get the full content of a cookie
        :return: list of cookie id as a string and a string of full cookie content
        """
        cookie_dict = self.get_cookie_dict()
        cookie_content = []
        for key, value in cookie_dict.items():
            if value not in ['', 0, []]:
                cookie_content.append(f'Your lucky {key}: {value}')
        return [cookie_dict['cookie id'], '\n'.join(cookie_content)]

def show_features():
    """
    Print existing and new features
    """
    print('Features:\n'
          '- Make a fortune cookie with a Confucius quote, lotto numbers, a power ball number, and a Chinese word.\n'
          '- Customize a fortune cookie with only a quote, lotto number, a power ball number, or a Chinese word.\n'
          '- Get unlimited amount of cookies until you call it quits.\n'
          '- Play with or without providing user information.\n'
          '- *NEW* Save all or selected fortune cookies to a text file on your computer.\n'
          '- *NEW* Send all or selected fortune cookies to your email.\n')


def show_help():
    """
    Display available commands and tutorials
    """
    print('Here is the full list of commands in alphabetic order. Type a command word at the cursor and enter return.\n'
          ' chinese    get a cookie with a Chinese word only.\n'
          ' cookie     get a cookie with all components.\n'
          ' exit       terminate the program.\n'
          ' features   show existing and new features.\n'
          ' help       show the full list of commands and tutorials.\n'
          ' lotto      get a cookie with lotto numbers only.\n'
          ' power      get a cookie with a powerball number only.\n'
          ' quote      get a cookie with a Confucius quote only.\n'
          ' save id1 id2 ...       save cookies with given ids to a local text file in the present working directory.\n'
          '         Separate id numbers by space for multiple cookies.\n'
          '         For example, "save 3 5 15" saves cookies with ids 3, 5, and 15; "save 3" saves cookie with id 3.\n'
          ' save -e id1 id2 ...    the e flag is used to send selected cookies to the email a user provided.\n'
          '         If an email is not provided, the command defaults to saving to a local tet file.\n'
          '         Separate the e flag and id number(s) by space.\n'
          '         For example, "save -e 3" saves cookie with id 3 to the provided email.\n'    
          ' saveall                save all cookies to a local text file in the present working directory.\n'
          ' saveall -e             the e flag is used to save all cookies to the email a user provided.\n'
          '         If an email is not provided, the command defaults to saving to a local tet file.\n')


def email_cookies(recipient, msg):
    # Create email
    load_dotenv()
    data = {

        # Sender parameters (variables pulled from .env file)
        "mail_server": os.getenv("SERVER"),
        "mail_port": os.getenv("PORT"),
        "mail_username": os.getenv("USERNAME"),
        "mail_password": os.getenv("PASSWORD"),

        # Email parameters (update with email data; can be taken from CLI or GUI)
        "recipients": [recipient],
        "subject": 'Fortune Cookies',
        "body": msg,

        # Optional parameters (can be deleted if not used)
        "html": False
        # "attachments": ["attachment1.txt", "attachment2.txt"]
    }

    # Send email
    url = 'http://localhost:5000/send-email'
    response = requests.post(url, json=data)
    print(response.json())

def validate_email(user):
    """
    Check if the user input of email address has valid syntax
    :param user: user dictionary
    :return: None
    """
    done_validating = 0
    while done_validating != 1:
        email = user['email']
        comm_file = open('ev-service.txt', 'w')
        comm_file.write(email)
        comm_file.close()

        # get response from the service
        while True:
            response_file = open('ev-service.txt', 'r')
            response = response_file.readline()
            if response == "valid":
                done_validating = edit_email(user, email)
                break
            elif response == "invalid":
                print("Your email address is invalid. Please try again.")
                retry_email(user)
                break

    with open('ev-service.txt', 'w') as comm_file2:
        comm_file2.write('done')

def edit_email(user, email):
    """
    Double check with user about keeping/removing/editing email
    :param user: user dictionary
    :param email: email input
    :return: 1 or 0
    """
    user_input = input(f"Do you want to email cookies to the following address: {email}? \n"
                       f"Enter 'y' to confirm. \n"
                       f"Enter 'rm' to remove the email. \n"
                       f"Enter any other key to provide a different email.\n" )
    command = user_input.lower()
    if command == "rm":
        user['email'] = ''
        print("Your email address is removed. You may proceed as a guest.\n")
        return 1
    elif command == "y":
        print("Your email address is saved. You may use it to get cookies later.\n")
        return 1
    else:
        retry_email(user)
        return 0


def retry_email(user):
    """
    Have user enter email address to update the user dictionary
    :param user: user dictionary
    :return: None
    """
    user_input = input("Please enter your email: ")
    user['email'] = user_input


def save_cookies(cookies, command, user):
    """
    Save the chosen or all cookies and exit program
    """
    # need to check if cookie id is out of range of cookies

    command_words = command.split(' ')
    saved_cookies = []
    if len(command_words) == 1:
        with open('cookies.json', 'w') as outfile:
            for cookie in cookies:
                saved_cookies.append(cookie.get_cookie_dict())
            json.dump(saved_cookies, outfile)
        print("All cookies are saved locally.\n")
    else:
        e_flag_or_not = command_words[1]
        if e_flag_or_not == "-e":
            user_email = user['email']
            if len(user_email) == 0:
                print("Your email was not provided. Restart the app to provide email or save the cookies locally.\n")
                return
            if command_words[0] == "saveall":
                # email all cookies
                # [LATER -MS: Format cookies]
                all_cookies = []
                for c in cookies:
                    all_cookies.append(c.get_cookie_content()[1])
                message = '\n\n'.join(all_cookies)
                email_cookies(user_email, message)
                print("All cookies are successfully sent via email. \n")
            else:
                # email these cookies
                selected_cookies = []
                for i in range(2, len(command_words)):
                    selected_cookie_id = int(command_words[i])
                    selected_cookies.append(cookies[selected_cookie_id - 1].get_cookie_content()[1])
                message = '\n\n'.join(selected_cookies)
                email_cookies(user_email, message)
                print("Your selected cookies are successfully sent via email\n")
        else:
            print("Your selected cookie ids are:")
            for i in range(1, len(command_words)):
                # save these cookies locally
                print(f'{command_words[i] }')
                cur_cookie = cookies[int(command_words[i]) - 1]
                saved_cookies.append(cur_cookie.get_cookie_dict())
            # IH8
            confirm_cookies = input("Are these the right cookies? Press 'y' to confirm, or any other key to cancel.\n")
            if confirm_cookies.lower() == "y":
                # ! fix wrong json format when appending
                # append selected cookies to a local file without erasing previous data
                # used the approach to append to json file from source: https://stackoverflow.com/questions/67904275/how-to-append-json-to-a-json-file
                with open('cookies-a.json', 'a') as outfile:
                    outfile.write(json.dumps(saved_cookies) + '\n')
                    # json.dump(saved_cookies, outfile)
            else:
                return
            print("Your selected cookies are saved locally.\n")
    print("You can start over, continue, or exit without losing the data.\n")



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
    print('A fresh batch of fortune cookies are in the oven. One moment...\n')

    # fetch quotes and words from github
    # url_quote = "https://github.com/wukongO-O/361-s24/blob/main/db-quotes.txt"
    # quotes, words = [], []
    # while len(quotes) == 0:
    #     quotes = fetch_github_db(url_quote)
    # url_word = "https://github.com/wukongO-O/361-s24/blob/main/db-words.txt"
    # while len(words) == 0:
    #     words = fetch_github_db(url_word)

    # fetch quotes and words from local txt files
    quotes = fetch_text_file_db('./db-quotes.txt')
    words = fetch_text_file_db('./db-words.txt')

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
    print("We will never sell your data. Your email will only be used to ship cookies.\n"
          "You will not be able to include an email later.\n")
    username = input("Your name: ")
    user['name'] = username

    email_add = input("Your email: ")
    user['email'] = email_add
    validate_email(user)

    while True:
        current_command = input("Type 'cookie' to get a new fortune cookie,\n "
                                "'quote' to get a cookie with quote only, \n"
                                "'lotto' to get a cookie with lottery numbers only, \n "
                                "'power' to get a cookie with a power ball number only, \n"
                                "'chinese' to get a cookie with Chinese word only, \n"
                                "or 'help' to see the full list of commands: \n")
        new_cookie = Cookie()
        new_cookie_id = len(cookies) + 1
        current_command = current_command.lower()

        # when user enters a non-cookie related command
        if current_command == "features":
            show_features()
            continue
        elif current_command == "help":
            show_help()
            continue
        elif re.search("^save.*", current_command):
            save_cookies(cookies, current_command, user)
            continue
        elif current_command == "exit":
            break

        # when user enters a cookie-related command
        if current_command == "cookie":
            new_cookie.make_full_cookie(new_cookie_id, quotes, words)
        elif current_command == "quote":
            new_cookie.customize_cookie(new_cookie_id, quotes, words, "quote")
        elif current_command == "lotto":
            new_cookie.customize_cookie(new_cookie_id, quotes, words, "lotto")
        elif current_command == "power":
            new_cookie.customize_cookie(new_cookie_id, quotes, words, "powerball")
        elif current_command == "chinese":
            new_cookie.customize_cookie(new_cookie_id, quotes, words, "chinese")
        else:
            print("Oops, this is not in our menu \n")
            continue

        cookies.append(new_cookie)
        new_cookie.show_cookie()



if __name__ == '__main__':
    main()
