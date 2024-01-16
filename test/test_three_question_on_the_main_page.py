from pages.main_page.main_page import MainPageQuestions
from pages.base_page import BasePage


class Test:
    # Проверяем открытие отображаемого ответа в вопросе
    def test_question_three(self, driver):
        main_page = MainPageQuestions(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        answer = main_page.question_three(driver)
        # Проверка, что после открытия ответа, отображается ожидаемый
        assert answer == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
