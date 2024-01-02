#!/usr/bin/python3
"""
module to fetch completed tasks
"""
import json
import sys
import urllib.request


if __name__ == "__main__":
    emp_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    url_user = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    
    with urllib.request.urlopen(url_user) as user:
        EMPLOYEE_NAME = json.loads(
                user.read().decode("utf-8")
            ).get("name")
        with urllib.request.urlopen(url) as raw_tasks:
            tasks = json.loads(
                raw_tasks.read().decode("utf-8")
            )
            TOTAL_NUMBER_OF_TASKS = len(tasks)
            done = [x for x in tasks if x.get('completed') is True]
            NUMBER_OF_DONE_TASKS = len(done)

            print(f"Employee {EMPLOYEE_NAME} ", end='')
            print(f"is done with tasks({NUMBER_OF_DONE_TASKS}/", end='')
            print(f"{TOTAL_NUMBER_OF_TASKS}):")

            for x in done:
                print(f"\t {x.get('title')}")
