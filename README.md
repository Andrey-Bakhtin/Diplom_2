# API-тесты для Stellar Burgers

## Описание

Автоматизированные API-тесты для сервиса Stellar Burgers.

## Стек технологий

* Python 3
* Pytest
* Requests
* Allure Report
* Faker

## Структура проекта

- api_methods/ - методы API
- tests/ - тестовые сценарии
- allure_results/ - сгенерированные отчёты Allure и вложения
- helpers.py - тестовые данные
- conftest.py - фикстуры pytest
- urls.py - URL-адреса
- requirements.txt - зависимости


## Base URL

https://stellarburgers.education-services.ru/

### Используемые эндпоинты

POST/api/auth/register - создание пользователя
POST/api/auth/login - авторизация пользователя
DELETE/api/auth/user - удаление пользователя
POST/api/orders - создание заказа

## Реализованные сценарии

Проект включает тесты для:
- создания пользователя с валидными данными;
- обработки попытки регистрации пользователя с существующим логином;
- обработки невалидных или отсутствующих полей при регистрации;
- авторизации существующего пользователя;
- обработки некорректных данных при авторизации;
- создания заказов авторизованным и неавторизованным пользователем.


## Установка

1. Создание виртуального окружения:
python3 -m venv .venv
source .venv/bin/activate

2. Установка зависимостей:
pip install -r requirements.txt

## Запуск тестов

Запуск всех тестов
pytest

Запуск с подробным выводом:
pytest -v

Запуск отдельного тестового файла:
pytest tests/test_create_user.py -v

## Генерация Allure-отчёта

Сбор результатов выполнения тестов:
pytest --alluredir=allure_results

Формирование и открытие отчёта:
allure serve allure_results
