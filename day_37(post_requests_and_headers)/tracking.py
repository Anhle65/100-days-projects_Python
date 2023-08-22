import requests
from datetime import datetime

# This work on pixela to create a graph for tracking workload
# -----------------------------------------------------------------------------------------
TOKEN = "afsgargrwhrhreahreg"
USER = "anhle"
WEBSITE = "https://pixe.la/v1/users"

# -----------------------------------------------------------------------------------------
# Create token and username to access
def create_user():

    parameter = {
        "token": TOKEN,
        "username": USER,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    access = requests.post(WEBSITE, json=parameter)
    print(access.text)

# -----------------------------------------------------------------------------------------
# Header is a parameter needed in other request
HEADER = {
    "X-USER-TOKEN": TOKEN
    }

# -----------------------------------------------------------------------------------------
# Post the overall interface on the created username with its token
def create_a_graph():
    post_graph = f"{WEBSITE}/{USER}/graphs"
    request_body = {
        "id": "graph1",
        "name": "Time to study",
        "unit": "minutes",
        "type": 'int',
        "color": "sora"
        }
    post = requests.post(post_graph, json=request_body, headers=HEADER)
    print(post.text)

# -----------------------------------------------------------------------------------------
# Using method strftime to get the date require format (see more format on W3 school-datetime module)
TODAY = datetime.now().strftime('%Y%m%d')

# -----------------------------------------------------------------------------------------
# Post the data including datetime and quantity
def post_pixel():
    total_time = input("How long have you studied: ")
    pixel_para = {
        "date": TODAY,
        "quantity": total_time,
        }
    post_pixel = f"{WEBSITE}/{USER}/graphs/graph1"
    post = requests.post(post_pixel, json=pixel_para, headers=HEADER)
    print(post.text)

# -----------------------------------------------------------------------------------------
# # Update the data including YYYYMMDD format datetime at last of the endpoint
def update_pixel():
    day = input("Which day you want to update the pixel (yyyy/mm/dd format): ")
    update_time = input("Update working time to: ")
    update_endpoint = f"{WEBSITE}/{USER}/graphs/graph1/{day}"
    update_infor = {
        "quantity": update_time
    }
    update = requests.put(update_endpoint, json=update_infor, headers=HEADER)
    print(update.text)

# -----------------------------------------------------------------------------------------
# Delete endpoint (delete the information post on that endpoint)
def delete_pixel():
    day = input("Which day you want to delete the pixel (yyyy/mm/dd format): ")
    delete_endpoint = f"{WEBSITE}/{USER}/graphs/graph1/{day}"
    response = requests.delete(delete_endpoint, params=delete_endpoint, headers=HEADER)
    print(response.text)
def main():
    print(f"u: Create a new user"
          f"g: Create a new graph"
          f"p: Post a pixel"
          f"u: Update the pixel"
          f"d: Delete the pixel")
    action = input("What you want to do? ").lower()
    condition = True
    while condition:
        if action == "u":
            create_user()
        elif action == "g":
            create_a_graph()
        elif action == "p":
            post_pixel()
        elif action == "u":
            update_pixel()
        elif action == "d":
            delete_pixel()
        else:
            condition = False

