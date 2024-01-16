from pages.order_page.order_page import OrderPage
from pages.main_page.main_page import LogoTesting
from pages.base_page import BasePage


class Test:
    # Проверяем возврат в главное меню, сперва открываем раздел
    # Заказать через кнопку в шапке, потом на логотип Самокат
    def test_jump_after_click_logo_car_in_header(self, driver):
        order_button = OrderPage(driver)
        logo_button = LogoTesting(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        # Кликаем Заказать в шапке
        order_button.order_for_header(driver)
        # Кликаем на логотип Самокат
        logo_button.jump_after_click_logo_car(driver)
        url = driver.current_url
        # Проверка, что открылась главная страница
        assert url == "https://qa-scooter.praktikum-services.ru/"

    # Проверяем возврат в главное меню, сперва открываем раздел
    # Заказать через кнопку в шапке, потом на логотип Самокат
    def test_jump_after_click_logo_car_in_footer(self, driver):
        order_button = OrderPage(driver)
        logo_button = LogoTesting(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        # Кликаем Заказать в шапке
        order_button.order_for_footer(driver)
        # Кликаем на логотип Самокат
        logo_button.jump_after_click_logo_car(driver)
        url = driver.current_url
        # Проверка, что открылась главная страница
        assert url == "https://qa-scooter.praktikum-services.ru/"
