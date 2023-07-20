import requests

endpoint = 'http://127.0.0.1:8000/api/update/good'

data = {
    "todo": "I'm fine",
    "completed": True
}

headers = {
    'Content-Type': 'application/json',
}

get_response = requests.put(endpoint, json=data, headers=headers)

print(get_response.status_code)