"""
https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
"""


from django.shortcuts import render, HttpResponse
import json # new
import requests # new 


# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = ''
        # --------------------------------------------------------------------------------->{api key}
        source = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={api_key}'
        list_of_data = requests.get(source.format(city)).json()
        
        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + " - " + str(list_of_data['coord']['lat']),
            'temp': round((list_of_data['main']['temp']-32) * 5.9/9.0, 2),
            'humidity' : str(list_of_data['main']['humidity']),
        }   
    else:
        data = {}
    return render(request, "home.html", data)

