import unittest
import requests
import json

from test.testGetToken import get_token


class TestEditToDo(unittest.TestCase):
    token = get_token()

    def test_edit_todo(self):
        try:
            url = "http://bzteltestapi.pythonanywhere.com/todos/testUser1/17"
            data = {
                "text": "Hi",
                "status": "DONE"
            }
            response = requests.put(url,
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer {}'.format(self.token)},
                                    json=data,
                                    timeout=0.8)
            request_json = json.loads(response.text)
            self.assertEqual(response.status_code, 202)
            self.assertEqual(request_json["result"], "Todo id:17 successfully updated!")
        except:
            self.fail("Request execution time exceeded")