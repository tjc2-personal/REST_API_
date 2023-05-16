# Run this only after running the API (main.py) I used uvicorn as the server.
import unittest
import requests

api_url = "http://localhost:8000/"

class TestValueStore(unittest.TestCase):

    def test_post(self):
        test_payload = {"label":"This is a test label."}
        header = {'Content-Type': 'application/json'}
        response = requests.post(api_url + 'item', headers=header, json=test_payload)

        if response.status_code == 200:
            complete = True
            item_data = response.json()
        else:
            raise Exception('Status code was not 200, ensure the target server is running.')

        self.assertTrue(complete)  # Comment because this assertion is lame, but basically boils down to status code.
        return item_data

    def test_get_all(self):
        response = requests.get(api_url + 'item/all')

        if response.status_code == 200:
            items = response.json()
            complete = True
        else:
            raise Exception('Status code was not 200, ensure the target server is running.')

        self.assertTrue(complete) # Comment because this assertion is lame, but basically boils down to status code.

    def test_get_id(self):
        id = self.test_post()
        url = api_url + "item/" + str(id['id'])
        response = requests.get(url)

        if response.status_code == 200:
            item = response.json()
            complete = True
        else:
            raise Exception('Status code was not 200, ensure the target server is running.')

        self.assertTrue(complete) # Comment because this assertion is lame, but basically boils down to status code.

if __name__ == "__main__":
    unittest.main()