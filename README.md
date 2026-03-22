# Sprint_9 — UI автотесты для сервиса Foodgram

Проект с UI-автотестами для сервиса **Foodgram / Продуктовый помощник**.  
Тесты написаны на Python + Selenium + Pytest + Allure с использованием паттерна Page Object.

---

## Что проверяется

### Создание аккаунта
- нажатие кнопки «Создать аккаунт»
- заполнение формы регистрации
- переход на страницу авторизации
- отображение формы авторизации

### Авторизация
- переход с главной страницы на форму входа
- ввод email и пароля
- переход на главную страницу
- отображение кнопки «Выход»

### Создание рецепта
- авторизация пользователя
- переход на страницу создания рецепта
- заполнение всех полей
- загрузка изображения
- создание рецепта
- проверка отображения созданной карточки рецепта

---

## Стек технологий

- Python
- Pytest
- Selenium
- Allure
- Faker
- Docker
- Docker Compose
- Selenoid
- GitHub Actions

---

## Структура проекта

SPRINT_9/
.github/workflows/ci.yml  
assets/  
config/browsers.json  
locators/  
pages/  
tests/  
utils/  
.dockerignore  
.gitignore  
conftest.py  
docker-compose.yml  
Dockerfile  
README.md  
requirements.txt  

---

## Установка зависимостей

Windows

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  

Linux / Mac

python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  

---

## Локальный запуск тестов

В utils/config.py

remote_driver = False

Запуск

pytest -v

Запуск конкретного файла

pytest tests/test_login_page.py -v  
pytest tests/test_create_account_page.py -v  
pytest tests/test_create_recipe_page.py -v  

---

## Allure отчёт

pytest --alluredir=allure-results

allure serve allure-results

или

allure generate allure-results -o allure-report --clean

---

## Запуск через Docker + Selenoid

В utils/config.py

remote_driver = True

Скачать браузер

docker pull selenoid/chrome:128.0

Поднять контейнеры

docker compose up -d --build

Запустить тесты

docker compose run --rm tests

Остановить

docker compose down -v

---

## Конфигурация Selenoid

config/browsers.json

{
  "chrome": {
    "default": "128.0",
    "versions": {
      "128.0": {
        "image": "selenoid/chrome:128.0",
        "port": "4444",
        "path": "/"
      }
    }
  }
}

---

## CI/CD

Workflow находится в

.github/workflows/ci.yml

Pipeline:

- собирает docker
- поднимает selenoid
- запускает тесты
- останавливает контейнеры

---

## Особенности реализации

- Page Object
- фикстуры pytest
- данные в utils/data.py
- локаторы отдельно
- без sleep
- только WebDriverWait
- загрузка файла через send_keys
- webdriver.Remote для Selenoid