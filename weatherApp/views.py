from django.shortcuts import render
import json
import urllib.request

#apikey = 'ClNwckAyebc63qmqsQV3wa0OyUBV0uCd'
# Create your views here.
def index(request):
    if request.method=='POST':
        cityName = request.POST['city']
        cityName2 = cityName.replace(' ', '+')
        responseResult = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+cityName2+'&appid=55b43b09f6828063e424f13ed60200a2').read()
        json_data = json.loads(responseResult)
        weather_Data = {
            "CountryCode" : str(json_data['sys']['country']),
            "lat" : str(json_data['coord']['lat']),
            "long" : str(json_data['coord']['lon']),
            "weatherDescription" : str(json_data['weather'][0]['description']).title(),
            "weatherIcon" : str(json_data['weather'][0]['icon']),
            "currentTemperature" : str(json_data['main']['temp'])+' Kelvin',
            "feelslike" : str(json_data['main']['feels_like'])+' Kelvin',
            "mintemp" : str(json_data['main']['temp_min'])+' Kelvin',
            "maxtemp" : str(json_data['main']['temp_max'])+' Kelvin',
            "pressure" : str(json_data['main']['pressure'])+' hPa',
            "humidity" : str(json_data['main']['humidity'])+'%',
            "windSpeed" : str(json_data['wind']['speed'])+' m/sec'
        }
    else:
        cityName = ''
        weather_Data = {}
    return render(request,'index.html',{'city':cityName,'weather_data':weather_Data})