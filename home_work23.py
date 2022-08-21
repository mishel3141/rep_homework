# Получить данные о погоде по апи (cайт и документация: https://www.metaweather.com/api/):
#  - сделать запрос по адресу https://www.metaweather.com/api/location/search/?query=kiev
#  - из ответа достать id погодной зоны, по ключу woeid
#  - сделать запрос по адресу https://www.metaweather.com/api/location/{woeid}/
#  - из ответа получить следующие данные: температура, влажность, скорость ветра.

import requests
from datetime import datetime

print('В связи с тем, что сайт www.metaweather.com работает неустойчиво,\n'
      'информация получена с сайта www.openweathermap.org')

URL_weather = "http://api.openweathermap.org/data/2.5/"    # Доступный сайт погоды
API_key = "c3ab06074043a039768ed8ef4a03891d"               # Получил при регистрации на сайте

town = input('\nПогоду в каком городе хотите знать: ')

params = {'appid': API_key, 'q': town, 'units': 'metric', 'lang': 'ru'}

''' Запрос на текущую погоду '''
req = requests.get(URL_weather + 'weather', params=params)

if req.status_code == 404:
      print('Это город, которого нет... ')
      exit(req.status_code)

x = req.json()

print('\nГород:', x['name'], ', страна:', x['sys']['country'],
      '(коорд:', x['coord']['lon'], 'д.,', x['coord']['lat'], 'ш.):')
print('Местное время:', datetime.fromtimestamp(x['dt']))
print('Погода:', x['weather'][0]['description'])
print('Температура:', x['main']['temp'], 'С', '(ощущается как', x['main']['feels_like'], 'С)')
print('Давление:', x['main']['pressure'], 'Па')
print('Влажность:', x['main']['humidity'], '%')
print('Скорость ветра:', x['wind']['speed'], 'м/с')
print('Восход солнца:', str(datetime.fromtimestamp(x['sys']['sunrise']))[10:],
      ', закат:', str(datetime.fromtimestamp(x['sys']['sunset']))[10:], '\n')

''' Запрос прогноза погоды на полдень завтра '''
req = requests.get(URL_weather + "forecast", params=params)
x = req.json()

print('Завтра в полдень ожидается: ')
print(' - погода:', x['list'][4]['weather'][0]['description'])
print(' - температура:', x['list'][4]['main']['temp'], 'С')
print(' - влажность:', x['list'][4]['main']['humidity'], '%')
print(' - скорость ветра:', x['list'][4]['wind']['speed'], 'м/с')
