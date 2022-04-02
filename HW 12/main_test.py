import pytest
from main import post_json, app


def test_json():
    data = {"name": "Alice"}
    response = app.test_client().post('/', json=data, follow_redirects=True)
    assert response.json == {"name_received" : "Alice"}