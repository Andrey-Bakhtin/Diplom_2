import requests
import allure

from urls import URL


class OrderMethods:

    @staticmethod
    @allure.step('Создать заказ с авторизацией')
    def create_order(body, token):
        return requests.post(url=URL.CREATE_ORDER, json=body, headers={'Authorization': token})
    
    @staticmethod
    @allure.step('Создать заказ без авторизации')
    def create_order_without_token(body):
        return requests.post(url=URL.CREATE_ORDER, json=body)
