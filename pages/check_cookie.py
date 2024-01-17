import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import Locators
from pages.base_page import BasePage
import time
import allure

# Проверка куки
class CheckCookie(BasePage):
    @allure.step('Закрытие куки')
    # Функция проверки наличия кнопки куки, если присутствует - кликаем
    def check_cookie(self, driver):
        time.sleep(10)
        cookie = driver.find_element(By.ID, Locators.cookie_message)
        if cookie:
            cookie.click()
        else:
            pass
