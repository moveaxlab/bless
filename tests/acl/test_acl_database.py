import os

import boto3
import pytest
from botocore.stub import ANY, Stubber

import bless.acl.acl_database as test
from bless.acl import acl_database
from tests.acl import dynamodb_vectors as vector

expected_params = {"Key": ANY, "TableName": ANY}


def test_mock_dynamodb():
    dynamodb = boto3.resource("dynamodb")
    stubber = Stubber(dynamodb.meta.client)
    stubber.add_response('get_item', vector.dynamodb_response_generic, expected_params)

    with stubber:
        service_response = dynamodb.Table("bless-acl-table").get_item(Key={"GroupId": "group_id"})

    assert service_response == vector.dynamodb_response_generic


@pytest.fixture
def dynamodb_resource_stub(autouse=True):
    with Stubber(test.dynamodb_resource.meta.client) as stubber:
        yield stubber
        stubber.assert_no_pending_responses()


def test_single_username(dynamodb_resource_stub):
    dynamodb_resource_stub.add_response(
        'get_item',
        vector.dynamodb_response_generic,
        expected_params={'Key': ANY}
    )
    result = test.get_valid_iam_principals('bogus-iam-user','bogus-acl-arn')