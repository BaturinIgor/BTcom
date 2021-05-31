import unittest
import requests
import json

from test.testGetToken import get_token


class TestAddToDo(unittest.TestCase):
    token = get_token()

    def test_add_delete_correct_todo(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            data = {
                "text": "Hello! It's ToDo!",
                "status": "TODO"
            }
            response = requests.post(url,
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(self.token)},
                                     json=data,
                                     timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(str(type(request_json["result"])), "<class 'str'>")
            self.assertEqual("New todo successfully created!", request_json["result"])
        except:
            self.fail("Request execution time exceeded")

        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            response = requests.get(url,
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer {}'.format(self.token)},
                                    timeout=0.8)
            request_json = json.loads(response.text)
        except:
            self.fail("Request execution time exceeded")

        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1/" + str(request_json[2]["id"])
            response = requests.delete(url,
                                       headers={'Content-Type': 'application/json',
                                                'Authorization': 'Bearer {}'.format(self.token)},
                                       timeout=0.8)
            request = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(str(type(request["result"])), "<class 'str'>")
            self.assertEqual("Todo id:" + str(request_json[2]["id"]) + " successfully deleted!", request["result"])
        except:
            self.fail("Request execution time exceeded")

    def test_add_delete_correct_in_progress(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            data = {
                "text": "Hello! It's InProgress!",
                "status": "INPROGRESS"
            }
            response = requests.post(url,
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(self.token)},
                                     json=data,
                                     timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(str(type(request_json["result"])), "<class 'str'>")
            self.assertEqual("New todo successfully created!", request_json["result"])
        except:
            self.fail("Request execution time exceeded")

        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            response = requests.get(url,
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer {}'.format(self.token)},
                                    timeout=0.8)
            request_json = json.loads(response.text)
        except:
            self.fail("Request execution time exceeded")

        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1/" + str(request_json[2]["id"])
            response = requests.delete(url,
                                       headers={'Content-Type': 'application/json',
                                                'Authorization': 'Bearer {}'.format(self.token)},
                                       timeout=0.8)
            request = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(str(type(request["result"])), "<class 'str'>")
            self.assertEqual("Todo id:" + str(request_json[2]["id"]) + " successfully deleted!", request["result"])
        except:
            self.fail("Request execution time exceeded")

    def test_add_delete_correct_done(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            data = {
                "text": "Hello! It's Done!",
                "status": "DONE"
            }
            response = requests.post(url,
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(self.token)},
                                     json=data,
                                     timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(str(type(request_json["result"])), "<class 'str'>")
            self.assertEqual("New todo successfully created!", request_json["result"])
        except:
            self.fail("Request execution time exceeded")

        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            response = requests.get(url,
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer {}'.format(self.token)},
                                    timeout=0.8)
            request_json = json.loads(response.text)
        except:
            self.fail("Request execution time exceeded")

        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1/" + str(request_json[2]["id"])
            response = requests.delete(url,
                                       headers={'Content-Type': 'application/json',
                                                'Authorization': 'Bearer {}'.format(self.token)},
                                       timeout=0.8)
            request = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(str(type(request["result"])), "<class 'str'>")
            self.assertEqual("Todo id:" + str(request_json[2]["id"]) + " successfully deleted!", request["result"])
        except:
            self.fail("Request execution time exceeded")

    def test_add_delete_correct_canceled(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            data = {
                "text": "Hello! It's Canceled!",
                "status": "CANCELED"
            }
            response = requests.post(url,
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(self.token)},
                                     json=data,
                                     timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(str(type(request_json["result"])), "<class 'str'>")
            self.assertEqual("New todo successfully created!", request_json["result"])
        except:
            self.fail("Request execution time exceeded")

        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            response = requests.get(url,
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer {}'.format(self.token)},
                                    timeout=0.8)
            request_json = json.loads(response.text)
        except:
            self.fail("Request execution time exceeded")

        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1/" + str(request_json[2]["id"])
            response = requests.delete(url,
                                       headers={'Content-Type': 'application/json',
                                                'Authorization': 'Bearer {}'.format(self.token)},
                                       timeout=0.8)
            request = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(str(type(request["result"])), "<class 'str'>")
            self.assertEqual("Todo id:" + str(request_json[2]["id"]) + " successfully deleted!", request["result"])
        except:
            self.fail("Request execution time exceeded")

    def test_add_delete_incorrect_status(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            data = {
                "text": "Hello! It's InProgress!",
                "status": "NEW"
            }
            response = requests.post(url,
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(self.token)},
                                     json=data,
                                     timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Status mast be 'TODO', 'INPROGRESS', 'DONE' or 'CANCELED'")
            self.assertEqual(str(type(request_json["message"])), "<class 'str'>")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_add_delete_empty_status(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            data = {
                "text": "Hello! It's InProgress!",
                "status": ""
            }
            response = requests.post(url,
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(self.token)},
                                     json=data,
                                     timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Empty fields: ['status']")
            self.assertEqual(str(type(request_json["message"])), "<class 'str'>")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")

    def test_add_delete_empty_text(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1"
            data = {
                "text": "",
                "status": "TODO"
            }
            response = requests.post(url,
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(self.token)},
                                     json=data,
                                     timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(request_json["message"], "Empty fields: ['text']")
            self.assertEqual(str(type(request_json["message"])), "<class 'str'>")
            self.assertEqual(response.status_code, 400)
        except:
            self.fail("Request execution time exceeded")