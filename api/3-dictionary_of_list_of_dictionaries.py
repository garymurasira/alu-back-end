#!/usr/bin/python3
"""returns information about
all tasks from all employees and save them in JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    users_resp = requests.get(f"{API_URL}/users")
    if users_resp.status_code != 200:
        sys.exit()
    users = users_resp.json()
    users_tasks = {}
    for user in users:
        tasks = requests.get(f"{API_URL}/users/{user['id']}/todos").json()

        users_tasks[user.get("id")] = []
        for task in tasks:
            task_dict = {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")}
            users_tasks[user.get("id")].append(task_dict)

    with open("todo_all_employees.json", "w") as file:
        json.dump(users_tasks, file)
