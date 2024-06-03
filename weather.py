import requests
import json

print(" Welcome to the Weather Location App!!\n")
print("This app helps you to detect your location temperature, day, date and time\n")
print("So Check your Location Weather!!\n")
city = input("Enter the name of the city or State: ")

# Create the URL for the WeatherAPI request
# Replace 'YOUR_API_KEY' with your actual API key
URL = f"http://api.weatherapi.com/v1/current.json?key=4c8fc4835fcd42e594d231853232208&q={city}"

response = requests.get(URL)  # Send GET request to the specified URL
data = json.loads(response.text)  # Parse the JSON response into a Python dictionary

# Extract location details from the response
location = data['location']
# Extract current weather details from the response
current = data['current']

# Print location details including city name,region,country
print(f"Location: {location['name']}\n") 
print(f"Location: {location['region']}\n")
print(f"Location: {location['country']}\n")
# Print the local time of the city
print(f"Local Time: {location['localtime']}\n")
# Print temperature in Celsius
print(f"Temperature: {current['temp_c']}°C\n") 
# Print temperature in Fahrenheit
print(f"Temperature: {current['temp_f']}°F\n")
# Print the weather condition description
print(f"Condition: {current['condition']['text']}\n")

# Thank you message 
print("Thank you for using our app!\n")
print("Have a great day ahead!Come Back Again!!!")