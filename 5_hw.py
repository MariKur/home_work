from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def check_elements() -> None:
    driver: WebDriver = webdriver.Chrome()

    try:
        # a. переход на страницу
        driver.get("https://www.saucedemo.com/")

        # b. поиск элементов
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        button = driver.find_element(By.ID, "login-button")

        # c. проверка
        if username and password and button:
            print("Элементы найдены")

    finally:
        driver.quit()


# вызов функции
check_elements()
