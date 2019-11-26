import os

import pytest
import boto3
from botocore.stub import Stubber, ANY

from bless.acl import acl_database

dynamodb_response = {
    "ConsumedCapacity": {
        "CapacityUnits": 1,
        "GlobalSecondaryIndexes": {
            "string": {
                "CapacityUnits": 1,
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
        },
        "LocalSecondaryIndexes": {
            "string": {
                "CapacityUnits": 1,
                "ReadCapacityUnits": 1,
                "WriteCapacityUnits": 1
            }
        },
        "ReadCapacityUnits": 1,
        "Table": {
            "CapacityUnits": 1,
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        },
        "TableName": "bless-acl-table",
        "WriteCapacityUnits": 1
    },
    "Item": {
        "string": {
            "SS": ["test"]  # Put here the values of the stubbed dynamoDB call
        }
    }
}

expected_params = {"Key": ANY,"TableName": ANY}


def test_mock_dynamodb():
    dynamodb = boto3.resource("dynamodb")
    stubber = Stubber(dynamodb.meta.client)
    stubber.add_response('get_item', dynamodb_response, expected_params)

    with stubber:
        service_response = dynamodb.Table("bless-acl-table").get_item(Key={"GroupId": "group_id"})

    assert service_response == dynamodb_response



@pytest.fixture
def dynamodb_resource():
    import boto3
    from botocore.stub import Stubber, ANY
    dynamodb = boto3.resource("dynamodb")
    stubber = Stubber(dynamodb.meta.client)
    return stubber
