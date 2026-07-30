import requests
import allure

from urls import URL


class UserMethods:

    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(body):
        return requests.post(url=URL.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Авторизовать пользователя в системе')
    def login_user(body):
        return requests.post(url=URL.LOGIN_USER, json=body)
    
    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(token):
        return requests.delete(url=URL.DELETE_USER, headers={'Authorization': token})
