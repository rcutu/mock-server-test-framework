from json import dumps
from uuid import uuid4
from pprint import pprint

import requests
from assertpy.assertpy import assert_that

from clients.mock_server import MockServerClient
from config import *

client = MockServerClient()


def test_get_metadata_for_first_subject():
    response = client.get_all_metadata(FIRST_SUBJECT)
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    pprint(response_text)
