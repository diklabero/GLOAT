import pytest
from Gloat.PageObjects.API import get_temp_data_api


@pytest.mark.sanity
class TestAPI:

    def test_weather(self):
        response = get_temp_data_api('20852', 'us', 'a734ea90e6c460c3f6843a5297952bde')
        response1 = get_temp_data_api('20852', 'us', 'a734ea90e6c460c3f6843a5297952bde')
        assert (abs(response - response1) / response) * 100.0 <= 10
