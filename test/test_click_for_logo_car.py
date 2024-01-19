import allure
from pages.order_page.order_page import OrderPage
from pages.main_page.main_page import LogoTesting
from pages.base_page import BasePage


class TestLogoCar:

    @allure.title('Переход на главную, через логотип Самокат (из меню Заказать в шапке)')
    # Проверяем возврат в главное меню, сперва открываем раздел
    # Заказать через кнопку в шапке, потом на логотип Самокат
    def test_jump_after_click_logo_car_in_header(self, driver):
        base_page = BasePage(driver)
        order_button = OrderPage(driver)
        logo_button = LogoTesting(driver)

        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        # Кликаем Заказать в шапке
        order_button.order_for_header()
        # Кликаем на логотип Самокат
        logo_button.jump_after_click_logo_car()
        url = base_page.current_url()
        # Проверка, что открылась главная страница
        assert url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Переход на главную, через логотип Самокат (из меню Заказать в футере)')
    # Проверяем возврат в главное меню, сперва открываем раздел
    # Заказать через кнопку в шапке, потом на логотип Самокат
    def test_jump_after_click_logo_car_in_footer(self, driver):
        order_button = OrderPage(driver)
        logo_button = LogoTesting(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        # Кликаем Заказать в шапке
        order_button.order_for_footer()
        # Кликаем на логотип Самокат
        logo_button.jump_after_click_logo_car()
        url = base_page.current_url()
        # Проверка, что открылась главная страница
        assert url == "https://qa-scooter.praktikum-services.ru/"
