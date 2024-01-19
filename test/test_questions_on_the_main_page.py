from pages.main_page.main_page import MainPageQuestions
from locators.main_page_locators import Locators
from pages.base_page import BasePage
import allure
import pytest


class TestMainQuestions:

    @allure.title('Проверяем список вопросов/ответов на главной странице')
    @pytest.mark.parametrize('button, answer, expected_result',
                             [(Locators.question_one_button, Locators.answer_question_one,
                               'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
                              (Locators.question_two_button, Locators.answer_question_two,
                               'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
                              (Locators.question_three_button, Locators.answer_question_three,
                               'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
                              (Locators.question_four_button, Locators.answer_question_four,
                               'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
                              (Locators.question_five_button, Locators.answer_question_five,
                               'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
                              (Locators.question_six_button, Locators.answer_question_six,
                               'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
                              (Locators.question_seven_button, Locators.answer_question_seven,
                               'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
                              (Locators.question_eight_button, Locators.answer_question_eight,
                               'Да, обязательно. Всем самокатов! И Москве, и Московской области.')])
    # Проверяем открытие отображаемого ответа в вопросе
    def test_questions(self, button, answer, expected_result, driver):
        main_page = MainPageQuestions(driver)
        base_page = BasePage(driver)
        base_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        get_answer = main_page.main_page_questions(button, answer)
        # Проверка, что после открытия ответа, отображается ожидаемый
        assert get_answer == expected_result
