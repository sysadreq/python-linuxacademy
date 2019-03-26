#!/usr/bin/env python3.6

import os
import requests
import sys
import argparse
import datetime


parser=argparse.ArgumentParser(description='get the current weather information for your zipcode')
parser.add_argument('zip',help="zip/postal code to get weather for")
parser.add_argument('--country', default='us', help='country zip/postal belongs to, default is US')
args=parser.parse_args()


api_key=os.getenv('OWM_API_KEY')

if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

url=f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res=requests.get(url)

if res.status_code != 200:
    print(f"error talking to weather provider: {res.status_code}")
    sys.exit(1)

weather_result = res.json()
temperature = int(weather_result['main']['temp']) - 273
w_descriptions = weather_result['weather'][0]['description']
w_sunrise = datetime.datetime.fromtimestamp(int(weather_result['sys']['sunrise'])).strftime('%Y-%m-%d %H:%M:%S')
w_sunset = datetime.datetime.fromtimestamp(int(weather_result['sys']['sunset'])).strftime('%Y-%m-%d %H:%M:%S')


print(f'Current weather in zipcode: {args.zip}')
print(f'Description: {w_descriptions}')
print(f'Temperature: {temperature} degress Celcius')

print(f'Sunrise: {w_sunrise}')
print(f'Sunset: {w_sunset}')