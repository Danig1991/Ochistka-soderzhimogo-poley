import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://www.saucedemo.com/"

# добавить опции
options = webdriver.ChromeOptions()

# оставить браузер открытым
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере
driver_chrome.get(base_url)

# команда для открытия окна в максимальном для монитора разрешении
driver_chrome.maximize_window()

# найти на странице элемент под id "user-name"
user_name = driver_chrome.find_element(By.ID, "user-name")

# пауза 1 секунда
time.sleep(1)

# установить в поле неверное значение
user_name.send_keys("invalid_value")
print("Ввод неверного логина.")

# пауза 1 секунда
time.sleep(1)

# выделить значение поля для логина
user_name.send_keys(Keys.CONTROL + "a")
print("Выделение значения поля для логина.")

# пауза 1 секунда
time.sleep(1)

# удалить значение поля логина
user_name.send_keys(Keys.DELETE)
print("Удаление значения поля логина.")

# пауза 1 секунда
time.sleep(1)

# установить в поле верное значение
user_name.send_keys("standard_user")
print("Ввод верного логина.")

# найти на странице элемент под id "password"
password = driver_chrome.find_element(By.ID, "password")

# пауза 1 секунда
time.sleep(1)

# установить в поле некорректный пароль
password.send_keys("incorrect_password")
print("Ввод некорректного пароля.")

# пауза 1 секунда
time.sleep(1)

# выделить значение поля для пароля
password.send_keys(Keys.CONTROL + "a")
print("Выделение значения поля для пароля.")

# пауза 1 секунда
time.sleep(1)

# удалить значение поля пароля
password.send_keys(Keys.DELETE)
print("Удаление значения поля пароля.")

# пауза 1 секунда
time.sleep(1)

# установить в поле корректный пароль
password.send_keys("secret_sauce")
print("Ввод корректного пароля.")

# пауза 1 секунда
time.sleep(1)

# найти на странице элемент под id "login-button"
login_button = driver_chrome.find_element(By.ID, "login-button")
# нажать на кнопку
login_button.click()
print("Нажатие на кнопку Login.")

# пауза 2,5 секунды
time.sleep(2.5)

# закрыть окно браузера
driver_chrome.close()
print("Окно закрыто.")