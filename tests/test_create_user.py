import pytest
import allure

from api_methods.user_methods import UserMethods
from helpers import generate_user_body


class TestCreateUser:
    
    @allure.title("Тест создания нового пользователя")
    @allure.description("""Тест проверяет успешное создание пользователя с использованием валидных данных. 
                         Ожидается: статус‑код 200; значение поля success в ответе равно True.""")
    def test_create_user_success(self):
        body = generate_user_body()
        response = UserMethods.create_user(body)
        response_data = response.json()
        token = response_data["accessToken"]
        assert response.status_code == 200
        assert response_data["success"] == True
        with allure.step("Удалить пользователя после теста"):
            UserMethods.delete_user(token)

    @allure.title("Тест создания пользователя с повторяющимся логином")
    @allure.description('''Тест проверяет обработку попытки создания пользователя с логином, который уже зарегистрирован.
                         Ожидается: статус‑код 403; сообщение об ошибке: «User already exists».''')
    def test_create_user_duplicate_login_shows_error(self, create_user_and_delete_after_test):
        with allure.step("Создать первого пользователя"):
            first_body = create_user_and_delete_after_test
        with allure.step("Создать второго пользователя с тем же логином"):
            second_user = UserMethods.create_user(first_body)
            second_user_data = second_user.json()
        with allure.step("Проверить результаты"):
            assert second_user.status_code == 403
            assert second_user_data["message"] == "User already exists"


    @allure.title("Тест создания пользователя с некорректными данными: {invalid_field} пуст")
    @allure.description('''Тест проверяет создание пользователя с пустым значением в обязательном поле {invalid_field}. 
                         Ожидается: статус‑код 403; cообщение: «Email, password and name are required fields».''')
    @pytest.mark.parametrize("invalid_field, invalid_value",
    [
        ("email", ""),
        ("password", ""),
        ("name", ""),  
    ])
    def test_create_user_empty_field_shows_error(self, invalid_field, invalid_value):
        with allure.step("Установить пустое значение для поля"):
            body = generate_user_body()
            body[invalid_field] = invalid_value
        with allure.step("Отправить запрос на создание пользователя"):
            response = UserMethods.create_user(body)
            response_data = response.json()
        with allure.step("Проверить результаты"):
            assert response.status_code == 403
            assert response_data["message"] == "Email, password and name are required fields"
