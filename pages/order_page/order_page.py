from locators.order_page_locators import Locators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('Открытие формы заказа, через кнопку "Заказ" в шапке')
    def order_for_header(self):
        self.check_cookie()
        self.find_element_located_click(Locators.order_button_in_header)

    @allure.step('Открытие формы заказа, через кнопку "Заказ" в футере')
    def order_for_footer(self):
        self.check_cookie()
        self.find_element_located_click(Locators.order_button_in_footer)

    @allure.step('Оформление заказа по заданным учеткам пользователей')
    def order_car(self, first_name, last_name, address, st_subway, phone, date, comment):
        self.find_element_located_click(Locators.order_button_in_header)
        self.find_element_located(Locators.first_name_field).send_keys(first_name)
        self.find_element_located(Locators.last_name_field).send_keys(last_name)
        self.find_element_located(Locators.address_field).send_keys(address)
        self.find_element_located_click(Locators.st_subway_field)
        self.find_element_located(Locators.st_subway_field).send_keys(st_subway)
        self.find_element_located(Locators.st_subway_field).send_keys(Keys.ARROW_UP)
        self.find_element_located(Locators.st_subway_field).send_keys(Keys.ENTER)
        self.find_element_located(Locators.phone_field).send_keys(phone)
        self.find_element_located_click(Locators.next_step_order_button)
        self.find_element_located(Locators.when_delivery_order).send_keys(date)
        self.find_element_located_click(Locators.time_rent)
        self.find_element_located_click(Locators.today_time_rent)
        self.find_element_located_click(Locators.black_color_car)
        self.find_element_located(Locators.comment_for_delivery).send_keys(comment)
        self.find_element_located_click(Locators.accept_order_button)
        self.find_element_located_click(Locators.complete_order_button)
        order_complete = self.find_element_located(Locators.order_info)
        return order_complete.text
