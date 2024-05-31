import json


def display_by_id():
    # use a json file to format into string
    sorted_result = ''
    with open('cookie_jar.json', 'r') as data_file:
        data = json.load(data_file)
        sorted_data = sorted(data, key=lambda x: x['cookie id'])
        for cookie_dict in sorted_data:
            for key, value in cookie_dict.items():
                if value not in ['', 0, []]:
                    sorted_result += f'{key}: {value}\n'
            sorted_result += '\n'

    return sorted_result


def display_by_type():
    sorted_result = ''
    with open('cookie_jar.json', 'r') as data_file:
        data = json.load(data_file)
        cookie_types = {
            "full": [],
            "quotes": [],
            "powers": [],
            "lottos": [],
            "words": []
        }
        for cookie in data:
            if '' not in cookie.values():
                cookie_types['full'].append(cookie)
            elif cookie['quote'] != '':
                cookie_types['quotes'].append(cookie)
            elif len(cookie['lotto']) != 0:
                cookie_types['lottos'].append(cookie)
            elif cookie['powerball'] != 0:
                cookie_types['powers'].append(cookie)
            elif cookie['chinese'] != '':
                cookie_types['words'].append(cookie)

        for c_type, c_list in cookie_types.items():
            if len(c_list) != 0:
                for cookie in c_list:
                    for key, value in cookie.items():
                        if value not in ['', 0, []]:
                            sorted_result += f'{key}: {value}\n'
                    sorted_result += '\n'

    return sorted_result


def read_request():
    """Read request from cj-service.txt"""
    data_str = ''
    with open('cj_service.txt', 'r') as data_file:
        data_str = data_file.readline().lower()
    return data_str


def write_response(result):
    """Write the display result into cj-service.txt"""
    with open('cj_service.txt', 'w') as comm_file:
        comm_file.write(result)


def main():
    print("Welcome to cookie jar. The service is listening to your request...")
    request = ''
    display_response = ''
    while request != 'done':
        with open('cj_service.txt', 'r') as data_file:
            request = data_file.readline().lower()
            if request == 'id':
                 display_response = display_by_id()
                 write_response(display_response)
            elif request == 'type':
                display_response = display_by_type()
                write_response(display_response)

    print("Your request is fulfilled. Thank you.")


if __name__ == '__main__':
    main()
