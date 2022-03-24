import requests
from datetime import datetime


APIKEY='66d968676154141c1088b3765dd91765'
URL_BASE='http://api.openweathermap.org/data/2.5/weather?'


city = input('Enter the city: ')

URL = f"{URL_BASE}q={city},&appid={APIKEY}"

response = requests.get(URL)


if response.status_code == 200:
	data = response.json()
	print('Country: ', data['sys']['country'])
	print('Temperature: ', round((data['main']['temp']-273),2), 'Celsius')
	print('Time: ', datetime.fromtimestamp(data['dt']))
	print('Sunrise: ', datetime.fromtimestamp(data['sys']['sunrise']))
	print('Sunset: ', datetime.fromtimestamp(data['sys']['sunset']))
	print('Cloud Conditions: ',data['weather'][0]['description'])
else:
	print('Server Error Occurred')
