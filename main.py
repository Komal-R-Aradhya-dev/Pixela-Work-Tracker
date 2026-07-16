import requests
import time
from datetime import datetime
import os

# --- Configuration ---
GRAPH_ID = "graph1"
USERNAME = "komalraradhya"
TOKEN = os.environ.get("PIXELA_TOKEN")
today = datetime.today().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
enter_data = f"{graph_endpoint}/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# --- Request Processing ---

# Data for Initial Post
data_params = {
    "date": today,
    "quantity": input("how many hour did u work today? "),
}

# --- Loop until success for posting data ---
success = False
attempts = 0
max_attempts = 10

while not success and attempts < max_attempts:
    response = requests.post(url=enter_data, headers=headers, json=data_params)
    result = response.json()

    if result.get("isSuccess"):
        print(f"Post Success! {result.get('message')}")
        success = True
    else:
        attempts += 1
        print(f"Attempt {attempts} failed: {result.get('message')}. Retrying in 2 seconds...")
        time.sleep(2)

if not success:
    print("Failed to post data after multiple attempts. Check your token or graph ID.")
else:
    # --- Updating data ---
    update_params = {
        "quantity": input("I hope u wanted to update u r working hours, kindly enter it here: "),
    }
    update_response = requests.put(url=update_endpoint, headers=headers, json=update_params)
    print(f"Update response: {update_response.text}")