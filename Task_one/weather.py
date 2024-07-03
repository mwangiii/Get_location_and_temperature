"""This module gets the temprature of the location"""
import requests
from apikey import api_keys

def get_weather(city):
    base_url = 'http://api.weatherapi.com/v1/current.json'
    query = f'?key={apikey}&q={city}'
    url = base_url + query

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['current']['temp_c']
    except requests.RequestException as error:
        raise Exception(f"HTTP error occurred: {error}")
    except KeyError:
        raise Exception(f"Failed to get temperature data for {city}")
