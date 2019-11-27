import boto3

dynamodb_resource = boto3.resource("dynamodb")
iam_client = boto3.client("iam")


def bless_prefix(args):
    if "bless-" in args:  # TODO do we have to set this as a configurable prefix?
        return True
    else:
        return False


def get_valid_iam_principals(iam_user, acl_arn):
    dynamodb = dynamodb_resource
    iam = iam_client
    groups = iam.list_groups_for_user(UserName=iam_user) or []
    userGroups = {group['GroupName'] for group in userGroups['Groups']}
    bless_groups = filter(bless_prefix, userGroups)
    group_roles = []
    try:
        for group in bless_groups:
            group_roles.extend(dynamodb.Table(acl_arn).get_item(Key={"GroupId": group})['Item']['Instances'])
    except Exception:
        return []
    return group_roles  # Returns an array of valid principals
