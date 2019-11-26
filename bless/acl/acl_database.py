"""
.. module: bless.ssh.acl_database
    :copyright: (c) 2019 by Moveax Ltd., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
"""

import boto3

def get_valid_iam_principals(iam_user, acl_arn):
    dynamodb = boto3.client("dynamodb")
    iam = boto3.client("iam")
    group_id = iam.list_groups_for_user(UserName=iam_user)
    try:
        group_roles = dynamodb.Table(acl_arn).get_item(Key={"GroupId": group_id})['Item']['Instances']
    except Exception:
        return ""
    return ",".join(group_roles) if not [] else "" # Returns a comma separated string of valid principals
