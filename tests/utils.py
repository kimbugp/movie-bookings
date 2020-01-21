import json


def registration(test_client, is_staff=True):
    data = json.dumps(
        {
            "email": "string@bb.com",
            "name": "string",
            "password": "dsfdsf",
            "is_staff": is_staff,
        }
    )
    response = test_client.post(
        "/api/v1/auth", data=data, headers={"Content-Type": "application/json"}
    )
    return response
