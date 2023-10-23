#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employeeId}"

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print(f"Employee {employee_name} is done with tasks({done}/{len(tasks)}):")

    for task in done_tasks:
        print(f"\t{task.get('title')}")
