import unittest
import requests
import json

from test.testGetToken import get_token


class TestGetIDToDo(unittest.TestCase):
    token = get_token()

    def test_edit_todo(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1/17"
            response = requests.get(url,
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer {}'.format(self.token)},
                                    timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            if not ("id" in request_json):
                self.fail("No ID field")
            if not ("text" in request_json):
                self.fail("No text field")
            if not ("status" in request_json):
                self.fail("No status field")
            if not ("create_time" in request_json):
                self.fail("No create_time field")
            if not ("update_time" in request_json):
                self.fail("No update_time field")
            self.assertEqual(str(type(request_json["id"])), "<class 'int'>")
            self.assertEqual(str(type(request_json["text"])), "<class 'str'>")
            self.assertEqual(str(type(request_json["status"])), "<class 'str'>")
            self.assertEqual(17, request_json["id"])
            self.assertEqual("Hi", request_json["text"])
            self.assertEqual("DONE", request_json["status"])
        except:
            self.fail("Request execution time exceeded")