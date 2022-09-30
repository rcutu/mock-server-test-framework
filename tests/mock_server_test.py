from json import dumps
from uuid import uuid4
from pprint import pprint

import requests
from assertpy.assertpy import assert_that

from config import BASE_URI


def test_get_metadata():
    response = requests.get(BASE_URI)
    response_text = response.json()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    pprint(response_text)
    for e in response_text:
        print(pprint(e))
