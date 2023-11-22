# utils.py

import requests
import base64

def get_movies():
    url = 'https://demo.credy.in/api/v1/maya/movies/'
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()}'
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Handle HTTP errors

    return response.json()['data']
