import json

import pytest

from tests.integration.api.test_main import client


@pytest.mark.incremental
class TestNewUserToDeleteUser:
    _url = "/user"
    _user_data = {
        "username": "pytest_user",
        "email": "pytest_user@gmail.com",
        "full_name": "pytest_user_full_name",
        "enabled": True,
        "password": "pytest_user_password"
    }
    _auth_header = {
        "Authorization": "Bearer aaaaaaa"
    }

    def test_add_add_new(self):
        body = self._user_data
        response = client.post(self._url, data=json.dumps(body))
        assert response.status_code == 201

    # def test_fail_to_change_status(self):
    #     params = {"desired_status": False}
    #     response = client.put(self._url + "/status", headers=self._auth_header, params=params)
    #     print(response.json())
    #     assert response.status_code == 401

    # def test_fail_to_subscribe(self):
    #     response = client.post("/subscription")

    def test_fail_to_delete(self):
        response = client.delete(self._url, headers=self._auth_header)
        assert response.status_code == 401

    def test_delete_user(self):
        body = {
            "username": self._user_data["username"],
            "password": self._user_data["password"],
            "grant_type": "",
            "scope": "",
            "client_id": "",
            "client_secret": ""
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        auth_response = client.post("/token", data=body, headers=headers)
        token = auth_response.json()["access_token"]
        self._auth_header["Authorization"] = f"Bearer {token}"
        response = client.delete(self._url, headers=self._auth_header)
        assert response.status_code == 200
