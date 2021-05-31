import unittest
import requests
import json


def get_token():
    url = "http://bzteltestapi.pythonanywhere.com/login"
    data = {
        "username": "testUser1",
        "password": "password1"
    }
    response = requests.post(url, json=data, timeout=0.8)
    request_json = json.loads(response.text)
    return request_json["access_token"]


class TestGetToken(unittest.TestCase):

    def test_get_correct_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
                "username": "testUser1",
                "password": "password1"
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertNotEqual(request_json["access_token"], "")
            self.assertEqual(str(type(request_json["access_token"])), "<class 'str'>")
            self.assertEqual(response.status_code, 200)
        except:
            self.fail("Request execution time exceeded")

    def test_get_incorrect_username_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
                "username": "HelloWorld",
                "password": "password1"
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "User HelloWorld not found")
            self.assertEqual(response.status_code, 404)
        except:
            self.fail("Request execution time exceeded")

    def test_get_incorrect_password_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
                "username": "testUser1",
                "password": "blablabla"
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "invalid password")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_empty_password_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
                "username": "testUser1",
                "password": ""
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Empty fields: ['password']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_empty_username_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
                "username": "",
                "password": "password1"
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Empty fields: ['username']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_empty_fields_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
                "username": "",
                "password": ""
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Empty fields: ['username', 'password']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_missing_password_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
                "username": "",
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Missing fields: ['password']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_missing_username_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
                "password": "",
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Missing fields: ['username']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_missing_fields_token(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/login"
            data = {
            }
            response = requests.post(url, json=data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Payload needed. No payload provided")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")