import requests

endpoint = 'http://127.0.0.1:8000/api/'

data = {
    'todo':"This is a new todo",
}

get_request = requests.post(endpoint, json=data)

print(get_request.json())
print(get_request.status_code)