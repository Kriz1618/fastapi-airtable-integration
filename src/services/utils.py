from typing import Any


def search_nested_values(dictionary: dict, search_key: str) -> Any:
    for key, value in dictionary.items():
        print('6', 'key', key)
        if isinstance(value, dict):
            result = search_nested_values(dictionary=value, search_key=key)
            if result is not None:
                return result
        elif key == search_key:
            return value


payload = {
    "timestamp": "2023-08-03T22:26:08.898Z",
    "baseTransactionNumber": 330,
    "actionMetadata": {
        "source": "client",
        "sourceMetadata": {
            "user": {
                "id": "usrX7vcxo72vATlQ1",
                "email": "christian.casaran@xmartlabs.com",
                "permissionLevel": "create",
                "name": "Christian Casaran",
                "profilePicUrl": "https://static.airtable.com/images/userIcons/user_icon_1.png"
            }
        }
    },
    "payloadFormat": "v0",
    "changedTablesById": {
        "tbliC0idApfr7aoEF": {
            "changedRecordsById": {
                "reccB8na7xw9Fy3sg": {
                    "current": {
                        "cellValuesByFieldId": {
                            "fld4OiNpmJbFlIpKv": "Vannessa Endi"
                        }
                    },
                    "unchanged": {
                        "cellValuesByFieldId": {
                            "fldhp884PdLvllban": "testing",
                            "fldrmVEG9W8OgC8bZ": {
                                "id": "seliBaGthOKr9clS5",
                                "name": "Inactive",
                                "color": "redBright"
                            }
                        }
                    }
                }
            }
        }
    }
}


print(search_nested_values(payload, 'changedRecordsById'))
