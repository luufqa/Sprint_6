from pages.order_page.order_page import OrderPage
from pages.base_page import BasePage
from pages.user_one import UserOne
from pages.user_two import UserTwo
import allure
import pytest


# Оформляем заказ через кнопку в шапке
class TestOrderForHeader:
    @allure.title('Оформление нового товара через кнопку Заказать в шапке')
    # Подставляем две разные учетки пользователя - с разными данными
    @pytest.mark.parametrize('first_name, last_name, address, st_subway, phone, date, comment, expected_result',
                             [(UserOne.first_name, UserOne.last_name, UserOne.address, UserOne.st_subway, UserOne.phone,
                               UserOne.date, UserOne.comment, 'Заказ оформлен'),
                              (UserTwo.first_name, UserTwo.last_name, UserTwo.address, UserTwo.st_subway, UserTwo.phone,
                               UserTwo.date, UserTwo.comment, 'Заказ оформлен')])
    # Оформление заказа через кнопку Заказать в шапке сайта
    def test_order_page_for_header(self, driver, first_name, last_name, address, st_subway, phone, date, comment,
                                   expected_result):
        # Передаем данные учетки пользователя
        page = OrderPage(driver, first_name, last_name, address, st_subway, phone, date, comment)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        page.order_for_header()
        order_for_header_button_complete = page.order_car()
        # Проверка успешного оформления заказа (появляется уведомление об успехе)
        assert expected_result in order_for_header_button_complete
