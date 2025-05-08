from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_current_weather(city_name='Dhaka'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv("API_KEY")}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Weather Condition ***')
    city = input('Please enter a city name: ')
    weather_data_main = get_current_weather(city)

    print(f'\nCurrent weather for {weather_data_main["name"]}')
    print(f'\nThe temperature is {weather_data_main["main"]["temp"]} degree C')
    print(f'\nFeels like {weather_data_main["main"]["feels_like"]} degree C and {weather_data_main["weather"][0]["description"].capitalize()}')
