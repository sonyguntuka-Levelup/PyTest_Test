from typing import Any
import pytest
from utils.apis import APIS
import uuid

@pytest.fixture(scope='module')
def apis():
    return APIS()

def test_getuser_validation(apis):
    response = apis.get(endpoint='users')
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_createuser_validation(apis, load_user_data):
    # user_data = {
    #     "name":"sony",
    #     "username":"sony QA",
    #     "email":"samplesony@gmail.com"     
    # }
    user_data = load_user_data["new user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email
    response = apis.post(endpoint='users', data=user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == "sony"

def test_updateuser_validation(apis):
    user_data = {
        "name":"Glenna Reichert 123"   
    }
    response = apis.put(endpoint='users/9', data=user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == "Glenna Reichert 123"

def test_deleteuser_validation(apis):
    response = apis.delete(endpoint='users/9')
    print(response.json())
    assert response.status_code == 200