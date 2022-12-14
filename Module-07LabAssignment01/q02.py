from math import ceil
from time import sleep
import requests
user_api = '2ecf0c820fdad418008324d3e0a25b3c'
def weather_data(city_name = 'Dhaka'):
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+user_api+"&units=metric"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    # print(api_data)
    if api_data['cod'] == '404':
         return print(f'{api_data["message"]}')
    else:
        return print(f'Temperature in {city_name} is {ceil(api_data["main"]["temp"])} Degree celsius')

while True:
    weather_data("dhaka")
    sleep(60*30)   
