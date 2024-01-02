#!/usr/bin/python3
"""
module to convert response to json file for all users
"""
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/todos'
    usr_url = 'https://jsonplaceholder.typicode.com/users'

    tasks = requests.get(url).json()
    users = requests.get(usr_url).json()

    my_dict = {}
    for user in users:
        task_list = []
        USR_ID = user.get('id')
        USR_NM = user.get('username')
        for task in tasks:
            if USR_ID == task.get('userId'):
                new_dict = {}
                new_dict["username"] = USR_NM
                new_dict['task'] = task.get('title')
                new_dict['completed'] = task.get('completed')
                task_list.append(new_dict)
        my_dict[USR_ID] = task_list

    with open('todo_all_employees.json', 'w') as my_file:
        json.dump(my_dict, my_file)
