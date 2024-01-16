from pages.main_page.main_page import MainPageQuestions
from pages.base_page import BasePage



class Test:
    # Проверяем открытие отображаемого ответа в вопросе
    def test_question_one(self, driver):
        main_page = MainPageQuestions(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        answer = main_page.question_one(driver)
        # Проверка, что после открытия ответа, отображается ожидаемый
        assert answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
