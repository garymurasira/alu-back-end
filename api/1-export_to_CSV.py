#!/usr/bin/python3
"""
fetch and and save todo lists for a user given their id
"""
import csv
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
    file_name = f"{sys.argv[1]}.csv"
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for task in todos:
            writer.writerow(
                [sys.argv[1], employee_userName,
                    str(task["completed"]), task["title"]]
                )


if __name__ == "__main__":
    main()
