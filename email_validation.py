# CS361
# Shenglan Li
# Microsevice B: email address validation
# Description: verify if the user email input is in valid address format
from time import sleep
import re

def read_request():
    """Read request from ev-service.txt"""
    email_address = ''
    while True:
        data_file = open('ev-service.txt', 'r')
        data_str = data_file.readline()
        if data_str not in ['valid', 'invalid', '']:
            email_address = data_str
            break
    data_file.close()
    return email_address


def write_response(result):
    """Write the verification result into ev-service.txt"""
    with open('ev-service.txt', 'w') as comm_file:
        comm_file.write(result)


def main():
    print("Welcome to email validation. The service is listening to your request...")
    email = ''
    while email != 'done':
        email = read_request()
        # Used method from the following link: https://stackoverflow.com/questions/65210754/how-to-validate-an-email-address-with-two-periods-in-it-python
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            write_response("valid")
        else:
            write_response("invalid")

    print("The validation is complete. Thank you.")


if __name__ == '__main__':
    main()

