import requests

response = requests.get("https://bnmapi-stage.azure-api.net/bnm-business/getProUsers/")
print(response.status_code)
print(response.json())

assert response.status_code == 200