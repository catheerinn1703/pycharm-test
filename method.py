import random

import requests

from test_data import base_url, create_user_payload, create_user_headers


def generate_username():
    random_integer = random.randint(1, 100)
    username = f"testing{random_integer}"
    return username


def register_contract(username):
    path = f"{base_url}/v2/user"
    response = requests.post(path, json=create_user_payload(username), headers=create_user_headers())
    return response, response.json()


def get_user_by_username(username):
    path = f"{base_url}/v2/user/{username}"
    response = requests.get(path)
    return response, response.json()
