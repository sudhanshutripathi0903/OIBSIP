city = input("Enter city name: ")

data = {
    "Sagar": {"temp": 28, "humidity": 62, "condition": "Clear"},
    "Bhopal": {"temp": 25, "humidity": 70, "condition": "Cloudy"},
    "Indore": {"temp": 27, "humidity": 55, "condition": "Sunny"}
}

if city in data:
    print("Temperature:", data[city]["temp"])
    print("Humidity:", data[city]["humidity"])
    print("Condition:", data[city]["condition"])
else:
    print("Weather data not available.")
