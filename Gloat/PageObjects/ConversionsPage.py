from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConversionsPage:
    __from_unit_locator = 'queryFrom'
    __to_unit_locator = 'queryTo'
    __value_to_convert_field_locator = '//h2[text()="{} to {}"]/following-sibling::div/input'
    __convert_button_locator = '//h2[text()="{} to {}"]/following-sibling::div/a[text()="Convert"]'
    __result_locator = 'answer'

    def __init__(self, driver):
        self.__driver = driver
        self.__driver.maximize_window()
        self.__wait = WebDriverWait(self.__driver, 10)

    def select_from_unit(self, from_unit):
        self.__driver.find_element(By.ID, self.__from_unit_locator).send_keys(from_unit)
        return self

    def select_to_unit(self, to_unit):
        self.__driver.find_element(By.ID, self.__to_unit_locator).send_keys(to_unit)
        return self

    def enter_value_to_convert(self, from_unit, to_unit, value):
        self.__wait.until(EC.presence_of_element_located((
              By.XPATH, self.__value_to_convert_field_locator.format(from_unit, to_unit)))).send_keys(value)
        return self

    def click_convert_button(self, from_unit, to_unit):
        self.__driver.find_element(By.XPATH, self.__convert_button_locator.format(from_unit, to_unit)).click()
        return self

    def enter_value_to_convert_and_click_convert_button(self, from_unit, to_unit, value):
        self.enter_value_to_convert(from_unit, to_unit, value)
        self.click_convert_button(from_unit, to_unit)

    def get_result(self):
        return self.__wait.until(EC.visibility_of_element_located((By.ID, self.__result_locator))).text
