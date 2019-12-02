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
    table_name = acl_arn.split('/')[1]
    userGroups = iam.list_groups_for_user(UserName=iam_user) or []
    userGroups = {group['GroupName'] for group in userGroups['Groups']}
    bless_groups = list(filter(bless_prefix, userGroups))
    group_roles = []
    tags = dynamodb.Table(table_name).scan()['Items']
    for tag in tags:
        for k in tag['Instances']:
            group_roles.append(k)

    group_roles = list(dict.fromkeys(group_roles))  # Make sure that there are no duplicates coming from multiple groups
    return group_roles  # Returns an array of valid principals
