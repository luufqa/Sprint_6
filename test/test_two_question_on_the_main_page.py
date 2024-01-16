from pages.main_page.main_page import MainPageQuestions
from pages.base_page import BasePage
import allure


class Test:
    @allure.title('После открытия второго ответа, отображается ожидаемый')
    # Проверяем открытие отображаемого ответа в вопросе
    def test_question_two(self, driver):
        main_page = MainPageQuestions(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        answer = main_page.question_two(driver)
        # Проверка, что после открытия ответа, отображается ожидаемый
        assert answer == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
