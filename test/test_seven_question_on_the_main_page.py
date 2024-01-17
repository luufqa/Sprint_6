from pages.main_page.main_page import MainPageQuestions
from pages.base_page import BasePage
import allure


class Test:
    @allure.title('После открытия седьмого ответа, отображается ожидаемый')
    # Проверяем открытие отображаемого ответа в вопросе
    def test_question_seven(self, driver):
        main_page = MainPageQuestions(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        answer = main_page.question_seven(driver)
        # Проверка, что после открытия ответа, отображается ожидаемый
        assert answer == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'