import pytest
import logging

from api_methods.user_methods import UserMethods
from helpers import generate_user_body


logger = logging.getLogger(__name__)

@pytest.fixture
def create_user_and_delete_after_test():
    body = generate_user_body()    
    response = UserMethods.create_user(body)
    yield body
    token = response.json()["accessToken"]
    delete_response = UserMethods.delete_user(token)
    if delete_response.status_code != 200:
        logger.warning(
            "Не удалось удалить пользователя с token %s. Статус: %s, Ответ: %s",
            token,
            delete_response.status_code,
            delete_response.json()
        )

@pytest.fixture
def authorized_user(create_user_and_delete_after_test):
    login_data = {
            "email": create_user_and_delete_after_test["email"],
            "password": create_user_and_delete_after_test["password"]
            } 
    login_response = UserMethods.login_user(login_data)
    token = login_response.json()["accessToken"]
    return token
