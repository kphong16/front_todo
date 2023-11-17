# requests_api.py
import requests


def fetch_data():
    response = requests.get("http://127.0.0.1:8000/todo/")
    data = response.json()
    return data
