dynamodb_response_generic = {
    "ConsumedCapacity": {
        "CapacityUnits": 1,
        "TableName": "bless-acl-table"
    },
    "Item": {
        "Instances": {
            "SS" :[
                "bless-bogus-response"
            ]
        }
    }
}

dynamodb_response_mvx_dev = {
    "ConsumedCapacity": {
        "CapacityUnits": 1,
        "TableName": "bless-acl-table"
    },
    "Item": {
        "Instances": {
            "SS" :[
                "bless-moveax-staging"
            ]
        }
    }
}

dynamodb_response_mvx_adm = {
    "ConsumedCapacity": {
        "CapacityUnits": 1,
        "TableName": "bless-acl-table"
    },
    "Item": {
        "Instances": {
            "SS" :[
                "bless-moveax-staging",
                "bless-moveax-production"
            ]
        }
    }
}

dynamodb_response_both_dev = {
    "ConsumedCapacity": {
        "CapacityUnits": 1,
        "TableName": "bless-acl-table"
    },
    "Item": {
        "Instances": {
            "SS" :[
                "bless-moveax-staging",
                "bless-moveax-production",
                "bless-othercorp-staging",
                "bless-othercorp-production"
            ]
        }
    }
}