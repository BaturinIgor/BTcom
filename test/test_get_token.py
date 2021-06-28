import unittest
import requests
import json


def get_token():
    url = "http://bzteltestapi.pythonanywhere.com/login"
    data = {
        "username": "testUser1",
        "password": "password1"
    }
    response = requests.post(url, json=data)
    request_json = json.loads(response.text)
    return request_json["access_token"]


class TestGetToken(unittest.TestCase):
    url = "http://bzteltestapi.pythonanywhere.com/login"
    username = "testUser1"
    password = "password1"

    def setUp(self) -> None:
        self.data = {
            "username": self.username,
            "password": self.password
        }

    def test_get_correct_token(self):
        response = requests.post(self.url, json=self.data)
        request_json = json.loads(response.text)
        self.assertNotEqual(request_json["access_token"], "")
        self.assertTrue(isinstance(request_json["access_token"], str))
        self.assertEqual(response.status_code, 200)

    def test_get_incorrect_username_token(self):
        try:
            self.data["username"] = "HelloWorld"
            response = requests.post(self.url, json=self.data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "User HelloWorld not found")
            self.assertEqual(response.status_code, 404)
        except:
            self.fail("Request execution time exceeded")

    def test_get_incorrect_password_token(self):
        try:
            self.data["password"] = "blablabla"
            response = requests.post(self.url, json=self.data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "invalid password")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_empty_password_token(self):
        try:
            self.data["password"] = ""
            response = requests.post(self.url, json=self.data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Empty fields: ['password']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_empty_username_token(self):
        try:
            self.data["username"] = ""
            response = requests.post(self.url, json=self.data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Empty fields: ['username']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_empty_fields_token(self):
        try:
            self.data["username"] = ""
            self.data["password"] = ""
            response = requests.post(self.url, json=self.data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Empty fields: ['username', 'password']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_missing_password_token(self):
        try:
            self.data["username"] = ""
            del self.data["password"]
            response = requests.post(self.url, json=self.data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Missing fields: ['password']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_missing_username_token(self):
        try:
            del self.data["username"]
            self.data["password"] = ""
            response = requests.post(self.url, json=self.data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Missing fields: ['username']")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_get_missing_fields_token(self):
        try:
            del self.data["username"]
            del self.data["password"]
            response = requests.post(self.url, json=self.data, timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Payload needed. No payload provided")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")
