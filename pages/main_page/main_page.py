from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import Locators
from pages.base_page import BasePage
from pages.check_cookie import CheckCookie


# Логотипы на главной странице
class LogoTesting(BasePage):
    # Кликаем по логотипу Самокат
    def jump_after_click_logo_car(self, driver):
        driver.find_element(By.XPATH, Locators.logo_car).click()

    # Кликаем по логотипу Яндекс
    def jump_after_click_logo_yandex(self, driver):
        driver.find_element(By.XPATH, Locators.logo_yandex).click()


# Вопросы на главной странице
class MainPageQuestions(BasePage):
    # Вопрос первый: Сколько это стоит? И как оплатить?
    def question_one(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        search_field = self.driver.find_element(By.ID, Locators.question_one_button)
        # Скроллим до кнопки с вопросом
        driver.execute_script("arguments[0].scrollIntoView();", search_field)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.question_one_button))
        )
        search_field.click()
        answer = self.driver.find_element(By.ID, Locators.answer_question_one).text
        # Возвращаем ответ на вопрос
        return answer

    # Вопрос второй: Хочу сразу несколько самокатов! Так можно?
    def question_two(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        # кликаем по кнопкам внутри конструктора и записываем их измененные классы

        search_field = self.driver.find_element(By.ID, Locators.question_two_button)
        # Скроллим до кнопки с вопросом
        driver.execute_script("arguments[0].scrollIntoView();", search_field)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.question_two_button))
        )
        search_field.click()
        answer = self.driver.find_element(By.ID, Locators.answer_question_two).text
        # Возвращаем ответ на вопрос
        return answer

    # Вопрос третий: Как рассчитывается время аренды?
    def question_three(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        # кликаем по кнопкам внутри конструктора и записываем их измененные классы

        search_field = self.driver.find_element(By.ID, Locators.question_three_button)
        # Скроллим до кнопки с вопросом
        driver.execute_script("arguments[0].scrollIntoView();", search_field)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.question_three_button))
        )
        search_field.click()
        answer = self.driver.find_element(By.ID, Locators.answer_question_three).text
        # Возвращаем ответ на вопрос
        return answer

    # Вопрос четвертый: Можно ли заказать самокат прямо на сегодня?
    def question_four(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        # кликаем по кнопкам внутри конструктора и записываем их измененные классы

        search_field = self.driver.find_element(By.ID, Locators.question_four_button)
        # Скроллим до кнопки с вопросом
        driver.execute_script("arguments[0].scrollIntoView();", search_field)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.question_four_button))
        )
        search_field.click()
        answer = self.driver.find_element(By.ID, Locators.answer_question_four).text
        # Возвращаем ответ на вопрос
        return answer

    # Вопрос пятый: Можно ли продлить заказ или вернуть самокат раньше?
    def question_five(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        # кликаем по кнопкам внутри конструктора и записываем их измененные классы

        search_field = self.driver.find_element(By.ID, Locators.question_five_button)
        # Скроллим до кнопки с вопросом
        driver.execute_script("arguments[0].scrollIntoView();", search_field)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.question_five_button))
        )
        search_field.click()
        answer = self.driver.find_element(By.ID, Locators.answer_question_five).text
        # Возвращаем ответ на вопрос
        return answer

    # Вопрос шестой: Вы привозите зарядку вместе с самокатом?
    def question_six(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        # кликаем по кнопкам внутри конструктора и записываем их измененные классы

        search_field = self.driver.find_element(By.ID, Locators.question_six_button)
        # Скроллим до кнопки с вопросом
        driver.execute_script("arguments[0].scrollIntoView();", search_field)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.question_six_button))
        )
        search_field.click()
        answer = self.driver.find_element(By.ID, Locators.answer_question_six).text
        # Возвращаем ответ на вопрос
        return answer

    # Вопрос седьмой: Можно ли отменить заказ?
    def question_seven(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        # кликаем по кнопкам внутри конструктора и записываем их измененные классы

        search_field = self.driver.find_element(By.ID, Locators.question_seven_button)
        # Скроллим до кнопки с вопросом
        driver.execute_script("arguments[0].scrollIntoView();", search_field)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.question_seven_button))
        )
        search_field.click()
        answer = self.driver.find_element(By.ID, Locators.answer_question_seven).text
        return answer

    # Вопрос Восьмой: Я жизу за МКАДом, привезёте?
    def question_eight(self, driver):
        # Функция проверки наличия кнопки куки, если присутствует - кликаем
        chk_cookie = CheckCookie(driver)
        chk_cookie.check_cookie(driver)
        search_field = self.driver.find_element(By.ID, Locators.question_eight_button)
        # Скроллим до кнопки с вопросом
        driver.execute_script("arguments[0].scrollIntoView();", search_field)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Locators.question_eight_button))
        )
        search_field.click()
        answer = self.driver.find_element(By.ID, Locators.answer_question_eight).text
        return answer
