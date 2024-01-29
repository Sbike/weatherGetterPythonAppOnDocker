import requests

def get_weather(city):
    api_key = "6be1b874ffe54576bd4145211242901"
    api_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(api_url)
    return response.json()

def display_weather(weather_data):
    location = weather_data['location']
    current = weather_data['current']
    print("-----------------------------------------------------")
    print(f"Weather Report for {location['name']}, {location['region']}, {location['country']}")
    print(f"Time: {location['localtime']}")
    print(f"Temperature: {current['temp_c']}°C / {current['temp_f']}°F")
    print(f"Condition: {current['condition']['text']}")
    print(f"Wind: {current['wind_mph']} mph / {current['wind_kph']} kph, Direction: {current['wind_dir']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Visibility: {current['vis_km']} km / {current['vis_miles']} miles")
    print(f"UV Index: {current['uv']}")
    print(f"Pressure: {current['pressure_mb']} mb / {current['pressure_in']} in")
    print(f"Cloud cover: {current['cloud']}%")
    print("-----------------------------------------------------")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)
