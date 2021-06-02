import requests
from datetime import datetime
# PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "asfghjklkjhgfded"
USERNAME = "ousman"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=parameters)
# print(response.text)

# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# PIXELA_ENDPOINT = "https://pixe.la/v1/users/ousman/graphs/graph1"
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# today = datetime.now()
# requests_body = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "15",
#
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=requests_body, headers=headers)
# print(response.text)


# *******************UPDATE PIXELA **************************

# PIXELA_ENDPOINT = "https://pixe.la/v1/users/ousman/graphs/graph1/20210502"
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# requests_body = {
#     "quantity": "15",
# }
# response = requests.put(url=PIXELA_ENDPOINT, json=requests_body, headers=headers)
# print(response.text)


# *******************DELETE PIXELA **************************

PIXELA_ENDPOINT = "https://pixe.la/v1/users/ousman/graphs/graph1/20210502"
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

response = requests.delete(url=PIXELA_ENDPOINT, headers=headers)
print(response.text)