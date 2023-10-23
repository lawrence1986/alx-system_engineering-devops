#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employeeId}"

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open(f"{employeeId}.csv", 'w') as file:
        for task in tasks:
            file.write(f'"{employeeId}","{username}","{task.get("completed")}","{task.get("title")}"\n')
