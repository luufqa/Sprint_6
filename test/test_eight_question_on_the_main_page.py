from pages.main_page.main_page import MainPageQuestions
from pages.base_page import BasePage


class Test:
    # Проверяем открытие отображаемого ответа в вопросе
    def test_question_eight(self, driver):
        main_page = MainPageQuestions(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        answer = main_page.question_eight(driver)
        # Проверка, что после открытия ответа, отображается ожидаемый
        assert answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'