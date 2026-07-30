import allure

from api_methods.order_methods import OrderMethods
from helpers import DataForOrder


class TestCreateOrder:

    @allure.title("Тест создания заказа авторизированным пользователем с валидными ингредиентами")
    @allure.description("""Тест проверяет успешное создание заказа с ингредиентами авторизированным пользователем.
                        Ожидается: статус‑код 200; значение поля success в ответе равно True.""")
    def test_create_order_autorized_success(self, authorized_user):
        token = authorized_user
        body = DataForOrder.VALID_INGREDIENTS
        response = OrderMethods.create_order(body, token)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True

    @allure.title("Тест создания заказа неавторизированным пользователем с валидными ингредиентами")
    @allure.description("""Тест проверяет успешное создание заказа с ингредиентами неавторизированным пользователем.
                        Ожидается: статус‑код 200; значение поля success в ответе равно True.""")
    def test_create_order_unautorized_success(self):
        body = DataForOrder.VALID_INGREDIENTS
        response = OrderMethods.create_order_without_token(body)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] == True

    @allure.title("Тест создания заказа с валидными ингредиентами")
    @allure.description("""Тест проверяет успешное создание авторизированным пользователем заказа с валидными ингредиентами.
                        Ожидается: статус‑код 200; наличие поля number в теле ответа (подтверждает успешное создание заказа и присвоение ему номера).""")
    def test_create_order_valid_ingredients_success(self, authorized_user):
        token = authorized_user
        body = DataForOrder.VALID_INGREDIENTS
        response = OrderMethods.create_order(body, token)
        response_data = response.json()
        assert response.status_code == 200
        assert "number" in response_data["order"]
   
    @allure.title("Тест создания заказа с неверным хешем ингредиентов")
    @allure.description("""Тест проверяет обработку попытки создания авторизированным пользователем заказа с неверным хешем ингредиентов.  
                        Ожидается: статус‑код 500.""")
    def test_create_order_invalid_ingredient_error(self, authorized_user):
        token = authorized_user
        body = DataForOrder.INVALID_INGREDIENT_HASH
        response = OrderMethods.create_order(body, token)
        assert response.status_code == 500

    @allure.title("Тест создания заказа без ингредиентов")
    @allure.description("""Тест проверяет обработку попытки создания авторизированным пользователем заказа без ингредиентов.  
                        Ожидается: статус‑код 400; сообщение об ошибке: «Ingredient ids must be provided».""")
    def test_create_order_without_ingredients_error(self, authorized_user):
        token = authorized_user
        body = DataForOrder.WITHOUT_INGREDIENTS
        response = OrderMethods.create_order(body, token)
        response_data = response.json()
        assert response.status_code == 400
        assert response_data["message"] == "Ingredient ids must be provided"
