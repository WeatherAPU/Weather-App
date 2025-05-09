import requests

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=427db18ead7081dbc93226b663a656ab&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        print(f"\nWeather forecast for {location.capitalize()}:")
        print(f"Condition: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} m/s")
    else:
        print(f"Error: Could not retrieve data for '{location}'. Please check the location name.")
def get_user_rating():
    while True:
        try:
            rating = int(input("\nRate this program from 1 to 5: "))
            if 1 <= rating <= 5:
                print(f"We appreciate you for rating us {rating} out of 5!")
                break
            else:
                print("Please rate the program between 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
            
def main():
    print("=== Weather Forecast App ===")
    location = input("Enter a city name: ").strip()
    if get_weather(location):
        get_user_rating()

if __name__ == "__main__":
    main()
