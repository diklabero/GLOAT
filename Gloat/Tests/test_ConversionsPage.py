import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Gloat.PageObjects.ConversionsPage import ConversionsPage


@pytest.mark.sanity
class TestSearch:
    __url = 'https://www.metric-conversions.org/'

    @pytest.fixture(scope='class', autouse=True)
    def setup_and_teardown(self):
        TestSearch.__driver = webdriver.Chrome(ChromeDriverManager().install())
        yield
        self.__driver.quit()

    @pytest.fixture(scope='function', autouse=True)
    def setup_and_teardown_function(self):
        self.__driver.get(f'{self.__url}')
        TestSearch.__conversion_page = ConversionsPage(self.__driver)
        yield
        pass

    @pytest.mark.parametrize("values", [['Celsius', 'Fahrenheit', '25', '25°C= 77.00000°F'],
                             ['Meters', 'Feet', '1', '1m = 3.2808ft'],
                             ['Ounces', 'Grams', '10', '10oz= 283.4952g']])
    def test_conversions(self, values):
        self.__conversion_page.select_from_unit(values[0])
        self.__conversion_page.enter_value_to_convert_and_click_convert_button(values[0], values[1], values[2])
        result = self.__conversion_page.get_result()
        assert result == values[3]
