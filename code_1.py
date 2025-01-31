import requests
import json

API_TOKEN = "pk_49001402_QFZKHCNMLP6SJ5LD3JBWGP4O78QA3C7T"
LIST_ID = "901805411539"
LIST_NAME = "LIST 1"
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
