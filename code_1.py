import requests
import json

API_TOKEN = "pk_89405806_PS9KTWYC6O5LQARWOE32IGOIP2SX9H03"
LIST_ID = "901805334349"
# LIST_NAME = "LIST 1"
LIST_NAME = "Sprint 49 (27/1/25 - 9/2/25)"

STATUS_FILTER = "TESTING"

# ClickUp API endpoint for tasks in a specific list
URL = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

# Headers for authentication
HEADERS = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

# Filtering tasks by status (TESTING)
PARAMS = {
    "status": "TESTING"
}

# Fetch tasks from ClickUp
response = requests.get(URL, headers=HEADERS, params=PARAMS)

if response.status_code == 200:
    tasks = response.json().get("tasks", [])  # Ensure 'tasks' key exists

    for task in tasks:
        # Extracting required details from the task
        task_name = task.get("name", "No Name")
        task_id = task.get("id", "No ID")
        assignees = ", ".join([assignee["username"] for assignee in task.get("assignees", [])]) if task.get("assignees") else "Unassigned"
        priority = (task.get("priority") or {}).get("priority", "No Priority")

        # Print only the required details
        print(f"Task ID: {task_id}\nTask Name: {task_name}\nAssignee: {assignees}\nPriority: {priority}\n")

else:
    print(f"Error: {response.status_code}, {response.text}")
