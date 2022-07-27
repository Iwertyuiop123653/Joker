import requests

def random_joke():
    headers = {
    'Content-type': 'application/json',
    }
    response = requests.get('https://icanhazdadjoke.com', headers=headers)
    print(response)
random_joke()