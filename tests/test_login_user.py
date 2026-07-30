import pytest
import allure

from api_methods.user_methods import UserMethods
from helpers import generate_random_email_password


class TestLoginUser:

    @allure.title("Тест успешной авторизации существующего пользователя")
    @allure.description("""Тест проверяет успешную авторизацию пользователя с валидными учётными данными.
                         Ожидается: статус‑код 200; значение поля success в ответе равно True.""")
    def test_login_user_existing_user_success(self, create_user_and_delete_after_test):
        with allure.step("Создать данные для авторизации"):
            login_data = {
            "email": create_user_and_delete_after_test["email"],
            "password": create_user_and_delete_after_test["password"]
            }
        with allure.step("Отправить запрос на логин пользователя"):
            response = UserMethods.login_user(login_data)
            response_data = response.json()
        with allure.step("Проверить результаты"):
            assert response.status_code == 200
            assert response_data["success"] == True

    @allure.title("Тест авторизации с некорректным значением для поля {key}")
    @allure.description("""Тест проверяет обработку авторизации при передаче некорректного значения в поле {key} 
                         и данные существующего пользователя во втором поле. 
                         Ожидается: статус‑код 401; сообщение: «email or password are incorrect».""")
    @pytest.mark.parametrize("key, value", [
        ("email", "test@yandex.ru"),
        ("password", "test")
    ])
    def test_login_user_with_incorrect_field_shows_error(self, create_user_and_delete_after_test, key, value):
        with allure.step("Создать данные для авторизации"):
            login_data = {
                "email": create_user_and_delete_after_test["email"],
                "password": create_user_and_delete_after_test["password"]
            }
            login_data[key] = value
        with allure.step("Отправить запрос на авторизацию пользователя"):
            response = UserMethods.login_user(login_data)
            response_data = response.json()
        with allure.step("Проверить результаты"):
            assert response.status_code == 401
            assert response_data["message"] == "email or password are incorrect"

    @allure.title("Тест авторизации пользователя с пустым значением для поля {key}")
    @allure.description("""Тест проверяет обработку авторизации при передаче пустого значения в поле {key}. 
                         Ожидается: статус‑код 401; сообщение: «email or password are incorrect».""")
    @pytest.mark.parametrize("key, value", [
        ("email", ""),
        ("password", "")
    ])
    def test_login_user_with_empty_field_shows_error(self, create_user_and_delete_after_test, key, value):
        with allure.step("Создать данные для авторизации"):
            login_data = {
                "email": create_user_and_delete_after_test["email"],
                "password": create_user_and_delete_after_test["password"]
                }
            login_data[key] = value
        with allure.step(f"Авторизация с пустым значением для поля {key}"):
            response = UserMethods.login_user(login_data)
            response_data = response.json()
        with allure.step("Проверить результаты"):
            assert response.status_code == 401
            assert response_data["message"] == "email or password are incorrect"

    @allure.title("Тест авторизации несуществующего пользователя")
    @allure.description("""Тест проверяет ответ системы при попытке авторизации несуществующего пользователя. 
                         Ожидается: статус‑код 401; сообщение: «email or password are incorrect».""")
    def test_login_user_with_nonexistent_user_shows_error(self):
        with allure.step("Авторизация с случайными учётными данными."):
            login_data = generate_random_email_password()
            response = UserMethods.login_user(login_data)
            response_data = response.json()
        with allure.step("Проверить результаты"):
            assert response.status_code == 401
            assert response_data["message"] == "email or password are incorrect"
            
