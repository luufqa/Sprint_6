from pages.main_page.main_page import MainPageQuestions
from pages.base_page import BasePage
import allure


class Test:
    @allure.title('После открытия пятого ответа, отображается ожидаемый')
    # Проверяем открытие отображаемого ответа в вопросе
    def test_question_five(self, driver):
        main_page = MainPageQuestions(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        answer = main_page.question_five(driver)
        # Проверка, что после открытия ответа, отображается ожидаемый
        assert answer == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'