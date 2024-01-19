from locators.main_page_locators import Locators
from pages.base_page import BasePage
import allure


# Логотипы на главной странице
class LogoTesting(BasePage):
    # Кликаем по логотипу Самокат
    @allure.step('Клик по логотипу Самокат')
    def jump_after_click_logo_car(self):
        self.find_element_located_click(Locators.logo_car)

    @allure.step('Клик по логотипу Самокат')
    # Кликаем по логотипу Яндекс
    def jump_after_click_logo_yandex(self):
        self.find_element_located_click(Locators.logo_yandex)


# Вопросы на главной странице
class MainPageQuestions(BasePage):
    @allure.step('Возвращаем значение ответа от требуемого вопроса')
    # Находим кнопку, скроллим, кликаем, возвращаем ответ на вопрос
    def main_page_questions(self, button, answer):
        self.check_cookie()
        search_field = self.find_element_located(button)
        self.execute_script(search_field)
        self.find_element_to_be_clickable(button)
        search_field.click()
        return self.find_element_located(answer).text
