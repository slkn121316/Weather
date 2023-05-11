from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
import requests

# Create your views here.

def city_location(request):
    try:
        city = request.POST.get('city', 'Noida')
        geo_api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},&appid=ff7b62320f8c6dfd3f38864f6b1a2c46"
        city_data = requests.get(geo_api_url).json()

        lat = city_data[0].get('lat', None)
        lon = city_data[0].get('lon', None)

        
        if lat is not None and lon is not None:
                weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=ff7b62320f8c6dfd3f38864f6b1a2c46&units=metric'
                weather_data = requests.get(weather_api_url).json()
                context = {'weather_data': weather_data}
        else:
                context = {'error_message': f"Couldn't get weather data for {city}"}

        return render(request, 'home/home1.html', context=context)
    
    except Exception as e:
        return HttpResponse("<h1>SORRY WE CANNOT FIND YOUR CITY</h1>")
