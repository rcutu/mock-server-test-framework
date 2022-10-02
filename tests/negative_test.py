import requests
from assertpy import assert_that, soft_assertions

from clients.mock_server_client import MockServerClient
from uuid import uuid4

from config import FIRST_SUBJECT

client = MockServerClient()


def test_read_invalid_subject():
    response = client.read_all_metadata(f'dummy{str(uuid4())}')
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    # after bug fix can be uncommented
    # with soft_assertions():
    #     assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    #     assert_that(response.text).is_equal_to("subject not found")


def test_query_invalid_subject():
    response = client.query_all_metadata([f'dummy{str(uuid4())}'])
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    # after bug fix can be uncommented
    # with soft_assertions():
    #     assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    #     assert_that(response.text).is_equal_to("subject not found")


def test_read_specific_metadata_with_wrong_subject():
    dummy_subject = f'dummy{str(uuid4())}'
    response = client.read_specific_metadata(dummy_subject, "name")
    assert_that(response.text).is_equal_to("Requested subject %r not found" %dummy_subject)
    # assert_that(response.status_code).is_equal_to(requests.codes.not_found)


def test_read_specific_metadata_with_property():
    dummy_property = "dummy_prop"
    response = client.read_specific_metadata(FIRST_SUBJECT, dummy_property)
    assert_that(response.text).is_equal_to("Requested property %r not found" % dummy_property)
    # assert_that(response.status_code).is_equal_to(requests.codes.not_found)


