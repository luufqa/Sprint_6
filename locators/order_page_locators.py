# Локаторы для Оформления заказа - order_page.py
class Locators:
    order_button_in_header = ".//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']"

    order_button_in_footer = ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    first_name_field = "//input[@placeholder='* Имя']"
    last_name_field = "//input[@placeholder='* Фамилия']"
    address_field = "//input[@placeholder='* Адрес: куда привезти заказ']"
    phone_field = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    st_subway_field = "//input[@placeholder='* Станция метро']"

    next_step_order_button = ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Далее']"

    when_delivery_order = ".//input[@placeholder='* Когда привезти самокат']"
    time_rent = ".//span[@class='Dropdown-arrow']"
    today_time_rent = ".//div[text()='сутки']"
    black_color_car = "black"
    comment_for_delivery = "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"

    accept_order_button = ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']"
    complete_order_button = ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Да']"

    order_info = ".//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']"
