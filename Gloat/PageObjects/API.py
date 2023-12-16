import json
import pytest
import requests


def get_weather_data_api(zipcode, country, api_key):
    content = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},'
                           f'{country}&appid={api_key}')
    return json.loads(content.text)


def get_temp_data_api(zipcode, country, api_key):
    return get_weather_data_api(zipcode, country, api_key)['main']['temp']
