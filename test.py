"""This file is for testing the server"""
import requests


BASE = "http://127.0.0.1:5000/"

# base url + the url we made
response = requests.get(BASE + "api/hello")
print(response.json())

# response = requests.post(BASE + "client")
# print(response.json())