import unittest
import requests
import json

from test.testGetToken import get_token


class TestGetToDos(unittest.TestCase):
    token = get_token()

    def test_get_correct_todos(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            response = requests.get(url,
                                    headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(self.token)},
                                    timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            if not ("id" in request_json[0]):
                self.fail("No ID field")
            if not ("text" in request_json[0]):
                self.fail("No text field")
            if not ("status" in request_json[0]):
                self.fail("No status field")
            if not ("create_time" in request_json[0]):
                self.fail("No create_time field")
            if not ("update_time" in request_json[0]):
                self.fail("No update_time field")
            self.assertNotEqual(len(request_json), 0)
            self.assertEqual(str(type(request_json[0]["id"])), "<class 'int'>")
            self.assertEqual(str(type(request_json[0]["text"])), "<class 'str'>")
            self.assertEqual(str(type(request_json[0]["status"])), "<class 'str'>")
        except:
            self.fail("Request execution time exceeded")