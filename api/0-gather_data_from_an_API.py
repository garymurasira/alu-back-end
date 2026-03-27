#!/usr/bin/python3
"""
fetch and display names, number of done tasks and names
of done tasks for a given user id
"""
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
    employee_name = user.get("name")

    todos_response = requests.get(f"{base}/todos",
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        sys.exit(1)
    todos = todos_response.json()

    completed = [task for task in todos if task.get("completed") is True]

    first_line = (
        f"Employee {employee_name} is done with tasks"
        f"({len(completed)}/{len(todos)}):"
    )
    print(first_line)

    for task in completed:
        title = task.get("title")
        print("\t {}".format(title))


if __name__ == "__main__":
    main()
