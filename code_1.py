import requests
import json

API_TOKEN = "pk_49001402_QFZKHCNMLP6SJ5LD3JBWGP4O78QA3C7T"
LIST_ID = "901805411539"
LIST_NAME = "LIST 1"
SUBTASK_ID = "86erdpe8b"  # Subtask ID that you provided

# ClickUp API endpoint for a specific subtask
SUBTASK_URL = f"https://api.clickup.com/api/v2/task/{SUBTASK_ID}"

# Headers for authentication
HEADERS = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

URL = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

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
# Function to fetch and display task and subtask details
def fetch_subtask_details(subtask_id):
    subtask_url = f"https://api.clickup.com/api/v2/task/{subtask_id}"
    response = requests.get(subtask_url, headers=HEADERS)

    if response.status_code == 200:
        subtask = response.json()

        # Print the subtask JSON for debugging
        
        subtask_name = subtask.get("name", "No Name")
        subtask_id = subtask.get("id", "No ID")
        assignees = ", ".join([assignee["username"] for assignee in subtask.get("assignees", [])]) if subtask.get("assignees") else "Unassigned"
        priority = (subtask.get("priority") or {}).get("priority", "No Priority")
        created_date = subtask.get("date_created", "No Date")

        print(f"Subtask ID: {subtask_id}\nSubtask Name: {subtask_name}\nAssignee: {assignees}\nPriority: {priority}\nCreated Date: {created_date}\n")
    else:
        print(f"Error fetching subtask {subtask_id}: {response.status_code}, {response.text}")

# Fetch and display the details of the subtask
fetch_subtask_details(SUBTASK_ID)
