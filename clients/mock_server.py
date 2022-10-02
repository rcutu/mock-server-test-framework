from config import *
import requests


class MockServerClient:
    def __init__(self):
        self.requests = None

    def post_all_metadata_for_tokens(self):
        requests.post(BASE_URI)

    def get_all_metadata(self, subject_id):
        return self.requests.get(f'{BASE_URI + subject_id}')

    def get_specific_metadata(self, subject_id, data_name):
        return self.requests.get(f'{BASE_URI + subject_id + data_name}')

