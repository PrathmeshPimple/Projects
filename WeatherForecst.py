# **** pip install requests ****  for installing the package used in program (paste in terminal and press 'Enter') 
import requests

def get_weather_data(location):
    # API endpoint and API key (you can get your own API key by signing up at openweathermap.org)
    api_endpoint = f"https://www.google.com/weatherforecaast"
    api_key = "204d98c01bc710a3ad738c8f9b97d87e"  # actual API key
    
    # Make the API request based on user input (city name or zip code)
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # You can change units to imperial for Fahrenheit
    }
    response = requests.get(api_endpoint, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse relevant weather information from the API response
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        
        # Return the weather information
        return temperature, humidity, description, wind_speed
    else:
        # If the request was not successful, return None
        print("Error retrieving data from the API.")
        return None

def main():
    # Prompt user for city name or zip code
    location = input("Enter city name or zip code: ")
    
    # Get weather data based on user input
    weather_info = get_weather_data(location)
    
    # Display weather information to the user
    if weather_info:
        temperature, humidity, description, wind_speed = weather_info
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Weather information not available.")

if __name__ == "__main__":
    main()
