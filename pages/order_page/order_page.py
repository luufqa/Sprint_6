from selenium.webdriver.common.by import By
from locators.order_page_locators import Locators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.check_cookie import CheckCookie


# Страница оформления заказа
class OrderPage(BasePage):
    def __init__(self, driver, first_name=None, last_name=None, address=None, st_subway=None, phone=None, date=None,
                 comment=None):
        super().__init__(driver)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.st_subway = st_subway
        self.phone = phone
        self.date = date
        self.comment = comment
    # Оформление заказа через кнопку Заказать - в шапке сайта
    def order_for_header(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.order_button_in_header))
        )
        # Кликаем по найденной кнопке Заказать в шапке
        driver.find_element(By.XPATH, Locators.order_button_in_header).click()

    # Оформление заказа через кнопку Заказать - в футере сайта
    def order_for_footer(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.order_button_in_footer))
        )
        # Кликаем по найденной кнопке Заказать в шапке
        driver.find_element(By.XPATH, Locators.order_button_in_footer).click()
    # Процедура оформления заказа по заданным аккаунтам  из параметризации
    def order_car(self, driver):
        driver.find_element(By.XPATH, Locators.order_button_in_header).click()
        driver.find_element(By.XPATH, Locators.first_name_field).send_keys(self.first_name)
        driver.find_element(By.XPATH, Locators.last_name_field).send_keys(self.last_name)
        driver.find_element(By.XPATH, Locators.address_field).send_keys(self.address)
        driver.find_element(By.XPATH, Locators.st_subway_field).click()
        driver.find_element(By.XPATH, Locators.st_subway_field).send_keys(self.st_subway)
        driver.find_element(By.XPATH, Locators.st_subway_field).send_keys(Keys.ARROW_UP)
        driver.find_element(By.XPATH, Locators.st_subway_field).send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, Locators.phone_field).send_keys(self.phone)
        driver.find_element(By.XPATH, Locators.next_step_order_button).click()
        driver.find_element(By.XPATH, Locators.when_delivery_order).send_keys(self.date)
        driver.find_element(By.XPATH, Locators.time_rent).click()
        driver.find_element(By.XPATH, Locators.today_time_rent).click()
        driver.find_element(By.ID, Locators.black_color_car).click()
        driver.find_element(By.XPATH, Locators.comment_for_delivery).send_keys(self.comment)
        driver.find_element(By.XPATH, Locators.accept_order_button).click()
        driver.find_element(By.XPATH, Locators.complete_order_button).click()
        order_complete = self.driver.find_element(By.XPATH, Locators.order_info).text
        # Возвращаем уведомление об успешном заказе
        return order_complete
