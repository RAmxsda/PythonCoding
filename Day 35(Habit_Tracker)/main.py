import requests
from datetime import datetime

USERNAME = "ramesh24"
TOKEN = "kdsjkadahskdjadssadui"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# user_response = requests.post(url=pixela_endpoint, json=user_params)
# print(user_response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": " Python Coding",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2.5",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# response.raise_for_status()
# print(response.text)

update_endpoint = (
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
)

new_pixel_data = {
    "quantity": "3.5",
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# delete_endpoint = (
#     f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
# )

# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)
