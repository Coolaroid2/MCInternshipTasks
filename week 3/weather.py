
import requests

api_key = "enter api key here"

def get_weather_data(api_key, city):
    api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"  
    response = requests.get(api_url)
    data = response.json()  
    temp = data['current']['temperature']
    icon = data['current']['weather_icons']
    description = data['current']['weather_descriptions']
    wdata = [temp, icon, description]
    return wdata

def main(city):
    weather_data = get_weather_data(api_key, city)
    return weather_data

if __name__ == '__main__':
    print(get_weather_data(api_key, 'Bangalore'))
