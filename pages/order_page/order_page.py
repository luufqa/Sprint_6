from locators.order_page_locators import Locators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.user_data import UserData
import allure


# Страница оформления заказа
class OrderPage(BasePage):
    def __init__(self, driver, first_name=None, last_name=None, address=None, st_subway=None, phone=None, date=None, comment=None):
        super().__init__(driver)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.st_subway = st_subway
        self.phone = phone
        self.date = date
        self.comment = comment

    # Оформление заказа через кнопку Заказать - в шапке сайта
    @allure.step('Открытие формы заказа, через кнопку "Заказ" в шапке')
    def order_for_header(self):
        self.check_cookie()
        # Кликаем по найденной кнопке Заказать в шапке
        self.find_element_located_click(Locators.order_button_in_header)

    # Оформление заказа через кнопку Заказать - в футере сайта
    @allure.step('Открытие формы заказа, через кнопку "Заказ" в футере')
    def order_for_footer(self):
        self.check_cookie()
        # Кликаем по найденной кнопке Заказать в футере
        self.find_element_located_click(Locators.order_button_in_footer)

    # Процедура оформления заказа по заданным аккаунтам  из параметризации
    @allure.step('Оформление заказа по заданным учеткам пользователей')
    def order_car(self):
        self.find_element_located_click(Locators.order_button_in_header)
        self.find_element_located(Locators.first_name_field).send_keys(self.first_name)
        self.find_element_located(Locators.last_name_field).send_keys(self.last_name)
        self.find_element_located(Locators.address_field).send_keys(self.address)
        self.find_element_located_click(Locators.st_subway_field)
        self.find_element_located(Locators.st_subway_field).send_keys(self.st_subway)
        self.find_element_located(Locators.st_subway_field).send_keys(Keys.ARROW_UP)
        self.find_element_located(Locators.st_subway_field).send_keys(Keys.ENTER)
        self.find_element_located(Locators.phone_field).send_keys(self.phone)
        self.find_element_located_click(Locators.next_step_order_button)
        self.find_element_located(Locators.when_delivery_order).send_keys(self.date)
        self.find_element_located_click(Locators.time_rent)
        self.find_element_located_click(Locators.today_time_rent)
        self.find_element_located_click(Locators.black_color_car)
        self.find_element_located(Locators.comment_for_delivery).send_keys(self.comment)
        self.find_element_located_click(Locators.accept_order_button)
        self.find_element_located_click(Locators.complete_order_button)
        order_complete = self.find_element_located(Locators.order_info)
        # Возвращаем уведомление об успешном заказе
        return order_complete.text
