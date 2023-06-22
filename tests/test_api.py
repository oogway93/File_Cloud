import requests
from fastapi import status


def test_root():
    response = requests.get("http://127.0.0.1:8000/file/get")
    assert response.status_code == status.HTTP_200_OK


def test_root_with_params():
    response = requests.get("http://127.0.0.1:8000/file/get?id=1")
    assert response.status_code == status.HTTP_200_OK
