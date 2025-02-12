import requests
import json

API_TOKEN = os.getenv("API_TOKEN")
LIST_ID = os.getenv("LIST_ID")
LIST_NAME = os.getenv("LIST_NAME")
SUBTASK_ID = os.getenv("SUBTASK_ID")  

HEADERS = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

URL = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"
SUBTASK_URL = f"https://api.clickup.com/api/v2/task/{SUBTASK_ID}"

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

def fetch_subtask_details(subtask_id):
    subtask_url = f"https://api.clickup.com/api/v2/task/{subtask_id}"
    response = requests.get(subtask_url, headers=HEADERS)

    if response.status_code == 200:
        subtask = response.json()

        
        subtask_name = subtask.get("name", "No Name")
        subtask_id = subtask.get("id", "No ID")
        assignees = ", ".join([assignee["username"] for assignee in subtask.get("assignees", [])]) if subtask.get("assignees") else "Unassigned"
        priority = (subtask.get("priority") or {}).get("priority", "No Priority")
        created_date = subtask.get("date_created", "No Date")

        print(f"Subtask ID: {subtask_id}\nSubtask Name: {subtask_name}\nAssignee: {assignees}\nPriority: {priority}\nCreated Date: {created_date}\n")
    else:
        print(f"Error fetching subtask {subtask_id}: {response.status_code}, {response.text}")

fetch_subtask_details(SUBTASK_ID)