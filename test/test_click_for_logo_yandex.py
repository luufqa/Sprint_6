import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page.main_page import LogoTesting
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Test:
    @allure.title('Переход в dzen, через логотип Яндекс')
    # Проверяем открытие сайта dzen, после клика на кнопку Яндекс
    def test_jump_after_click_logo_yandex(self, driver):
        logo_button = LogoTesting(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        # Кликаем на логотип Яндекс
        logo_button.jump_after_click_logo_yandex(driver)
        # Меняем активное окно
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        # Ожидаем загрузки сайта
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "__SVG_SPRITE_NODE__")))
        url = driver.current_url
        # Проверка, что открылась страница dzen
        assert "https://dzen.ru/" in url