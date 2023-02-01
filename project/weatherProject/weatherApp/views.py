from django.shortcuts import render

# Create your views here.

import urllib.request
import json

def index (request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=9e6f5da9f848e7b683f79045e338f769').read()
        # Because we workwith APIs, openweathermap.org it generate a unique API the moment that you made an account. Therefore, if you want to copy this API
        # from above it will not work for you being my personal generated API. What you need to do is to go on the website, make an account, and then
        # after log in you will find your own API. Copy it and paste it where it need to be: 
        # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + 
        # city + '&units=metric&appid=<Your API from https://openweathermap.org/api account>').read()
        
        # convert the json into a dictionary
        list_of_data = json.loads(source) 
        # dictionary
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
