import requests
from datetime import datetime

# This work on pixela to create a graph for tracking workload
# -----------------------------------------------------------------------------------------
TOKEN = "afsgargrwhrhreahreg"
USER = "anhle"

# -----------------------------------------------------------------------------------------
# Create token and username to access
parameter = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
website = "https://pixe.la/v1/users"
access = requests.post(website, json=parameter)
print(access.text)

# -----------------------------------------------------------------------------------------
# # Header is a parameter needed in other request
header = {
    "X-USER-TOKEN": TOKEN
    }

# -----------------------------------------------------------------------------------------
# # Post the overall interface on the created username with its token
post_graph = f"{website}/{USER}/graphs"
request_body = {
    "id": "graph1",
    "name": "Time to study",
    "unit": "minutes",
    "type": 'int',
    "color": "sora"
    }
post = requests.post(post_graph, json=request_body, headers=header)
print(post.text)

# -----------------------------------------------------------------------------------------
# # Using method strftime to get the date require format (see more format on W3 school-datetime module)
today = datetime.now().strftime('%Y%m%d')

# -----------------------------------------------------------------------------------------
# # Post the data including datetime and quantity
pixel_para = {
    "date": today,
    "quantity": "60",
    }
post_pixel = f"{website}/{USER}/graphs/graph1"
post = requests.post(post_pixel, json=pixel_para, headers=header)
print(post.text)

# -----------------------------------------------------------------------------------------
# # Update the data including YYYYMMDD format datetime at last of the endpoint
update_endpoint = f"{website}/{USER}/graphs/graph1/{today}"
update_infor = {
    "quantity": "80"
}
update = requests.put(update_endpoint, json=update_infor, headers=header)
print(update.text)

# -----------------------------------------------------------------------------------------
# # Delete endpoint (delete the information post on that endpoint)
delete_endpoint = f"{website}/{USER}/graphs/graph1/{today}"
response = requests.delete(delete_endpoint, params=delete_endpoint, headers=header)
print(response.text)