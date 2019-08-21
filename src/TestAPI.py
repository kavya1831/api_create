
import requests


def testUserAPI():
    dummy_json ={
    "name": "kavya",
    "age": 21,
    "email": "kkm18311@gmail.com",
    "password": "destiny318"
    }
    url = "http://localhost:8081/user/"
    response = requests.post(url, json=dummy_json)
    print response.json()

testUserAPI()
