#!/usr/bin/python3
"""
Using a REST API, and a given emp_ID, return info about their TODO list.
"""
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    base_url = "http://jsonplaceholder.typicode.com"

    user = requests.get(base_url + "/users/{}".format(emp_id)).json()
    todos = requests.get(base_url + "/todos?userId={}".format(emp_id)).json()

    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len(done_tasks),
        len(todos)
    ))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
