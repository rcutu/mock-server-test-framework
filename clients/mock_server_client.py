from config import *
from json import dumps
from clients.base_client import BaseClient
from utils.request import APIRequest


class MockServerClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI
        self.request = APIRequest()
        self.query_url = self.base_url + "query"

    def query_all_metadata(self, subjects):
        payload = dumps({"subjects": subjects})
        return self.request.post(self.query_url, payload, self.headers)

    def query_specific_metadata(self, subjects, properties):
        payload = dumps({"subjects": subjects,
                         "properties": properties})
        return self.request.post(self.query_url, payload, self.headers)

    def read_all_metadata(self, subject_id):
        return self.request.get(f'{self.base_url + subject_id}')

    def read_specific_metadata(self, subject_id, property_name):
        url = self.base_url + subject_id + "/properties/" + property_name
        return self.request.get(url)


