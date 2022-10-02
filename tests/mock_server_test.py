import requests
from assertpy.assertpy import *

from clients.mock_server_client import MockServerClient
from config import *
from utils.compare import compare

client = MockServerClient()


def test_read_metadata_for_first_subject():
    response = client.read_all_metadata(FIRST_SUBJECT)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
        assert_that(response.as_dict).contains_key("subject")
        assert_that(response.as_dict).contains_value(FIRST_SUBJECT)
        for e in known_properties:
            assert_that(response.as_dict).contains_key(e)


def test_read_metadata_for_second_subject():
    response = client.read_all_metadata(SECOND_SUBJECT)

    with soft_assertions():
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
        assert_that(response.as_dict).contains_key("subject")
        assert_that(response.as_dict).contains_value(SECOND_SUBJECT)
        for e in known_properties:
            assert_that(response.as_dict).contains_key(e)


def test_query_output_against_read_for_first_subject():
    response_by_read = client.read_all_metadata(FIRST_SUBJECT)
    response_by_query = client.query_all_metadata([FIRST_SUBJECT])

    with soft_assertions():
        assert_that(response_by_read.status_code).is_equal_to(requests.codes.ok)
        assert_that(response_by_query.status_code).is_equal_to(requests.codes.ok)
        assert_that(response_by_query.as_dict['subjects'][0]).is_equal_to(response_by_read.as_dict)


def test_query_output_against_read_for_both_subjects():
    first_subject_response = client.read_all_metadata(FIRST_SUBJECT)
    second_subject_response = client.read_all_metadata(SECOND_SUBJECT)
    response_by_query = client.query_all_metadata([FIRST_SUBJECT, SECOND_SUBJECT])

    with soft_assertions():
        assert_that(first_subject_response.status_code).is_equal_to(requests.codes.ok)
        assert_that(second_subject_response.status_code).is_equal_to(requests.codes.ok)
        assert compare(response_by_query.as_dict["subjects"],
                       [first_subject_response.as_dict,
                        second_subject_response.as_dict]), "The two lists are not the same"


def test_specific_metadata_for_subject_against_query():
    for e in known_properties:
        first_subject_response = client.read_specific_metadata(FIRST_SUBJECT, e)
        first_subject_response_by_query = client.query_specific_metadata([FIRST_SUBJECT], [e])
        with soft_assertions():
            assert_that(first_subject_response.status_code).is_equal_to(requests.codes.ok)
            assert_that(first_subject_response_by_query.status_code).is_equal_to(requests.codes.ok)

        name_by_query = first_subject_response_by_query.as_dict["subjects"][0][e]
        assert compare(name_by_query, first_subject_response.as_dict), "Maps are different"
