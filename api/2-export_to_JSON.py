#!/usr/bin/python3
"""
fetch and and save todo lists for a user given their id to a json file
"""
import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} EMPLOYEE_ID", file=sys.stderr)
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("id must be an integer", file=sys.stderr)
        sys.exit(1)

    base = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base}/users/{employee_id}")
    if user_response.status_code != 200:
        sys.exit(1)
    user = user_response.json()
    employee_userName = user.get("username")

    todos_response = requests.get(f"{base}/todos",
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        sys.exit(1)
    todos = todos_response.json()
    id = sys.argv[1]
    user_tasks = {id: []}
    for task in todos:
        tasks = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_userName
        }
        user_tasks[id].append(tasks)

    with open(f"{id}.json", "w") as file:
        json.dump(user_tasks, file)


if __name__ == "__main__":
    main()
