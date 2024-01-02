#!/usr/bin/python3
"""
module to fetch tasks and save as csv
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    tasks_url = f'https://jsonplaceholder.typicode.com/users/{USER_ID}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{USER_ID}'
    tasks = requests.get(tasks_url).json()
    USERNAME = requests.get(user_url).json().get("username")
    output = []
    tasks_len = len(tasks)
    for idx in range(tasks_len):
        task = tasks[idx]
        STATUS = task.get('completed')
        TITLE = task.get('title')
        output.append(f"{USER_ID},{USERNAME},{STATUS},{TITLE}".split(','))

    with open(f"{USER_ID}.csv", "w")as csvFile:
        write = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        write.writerows(output)
