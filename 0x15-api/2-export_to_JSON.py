#!/usr/bin/python3
"""
module to convert response to json file
"""
import json
import requests
import sys

if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    usr_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    data = requests.get(url).json()
    usr_data = requests.get(usr_url).json().get('username')

    data_list = []
    for info in data:
        new_dict = {}
        new_dict['task'] = info.get('title')
        new_dict['completed'] = info.get('completed')
        new_dict['username'] = usr_data
        data_list.append(new_dict)
    my_dict = {emp_id: data_list}

    with open(f'{emp_id}.json', 'w') as my_file:
        json.dump(my_dict, my_file)
