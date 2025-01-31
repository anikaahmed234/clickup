import requests
import json

API_TOKEN = ""
LIST_ID = ""
LIST_NAME = "LIST 1"
# LIST_NAME = "Sprint 49 (27/1/25 - 9/2/25)"

STATUS_FILTER = "TESTING"

URL = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

HEADERS = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

PARAMS = {
    "status": "TESTING"
}

response = requests.get(URL, headers=HEADERS, params=PARAMS)

if response.status_code == 200:
    tasks = response.json().get("tasks", []) 

    for task in tasks:
        task_name = task.get("name", "No Name")
        task_id = task.get("id", "No ID")
        assignees = ", ".join([assignee["username"] for assignee in task.get("assignees", [])]) if task.get("assignees") else "Unassigned"
        priority = (task.get("priority") or {}).get("priority", "No Priority")
        print(f"Task ID: {task_id}\nTask Name: {task_name}\nAssignee: {assignees}\nPriority: {priority}\n")

else:
    print(f"Error: {response.status_code}, {response.text}")
