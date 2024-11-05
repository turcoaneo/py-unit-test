import json
import unittest

from app import app


class TestApi(unittest.TestCase):
    def test_endpoint_return_ok(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Dirk Verbeuren is in a good band"})
            assert response._status_code == 200

    def test_json_body(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Kamala Harris"})
            data = json.loads(response.get_data())
            assert len(data['entities']) > 0
            self.assertEqual("Kamala Harris", data['entities'][0]["ent"])
            self.assertEqual("Person", data['entities'][0]["label"])
