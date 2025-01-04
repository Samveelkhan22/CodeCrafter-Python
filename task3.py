import socket
import json
from functools import reduce

# Mock weather data for simulation
MOCK_WEATHER_DATA = {
    "London": {"temperature": 15.0, "weather": "light rain"},
    "New York": {"temperature": 25.0, "weather": "clear sky"},
    "Sydney": {"temperature": 22.0, "weather": "few clouds"},
    "Mumbai": {"temperature": 30.0, "weather": "clear sky"},
    "Tokyo": {"temperature": 18.0, "weather": "scattered clouds"},
}

# Server Code (Runs in a thread to simulate network behavior)
def weather_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 65432))
    server.listen(1)
    print("Weather server running...")

    while True:
        conn, addr = server.accept()
        print(f"Connection from {addr}")
        data = conn.recv(1024).decode()
        requested_cities = json.loads(data)
        response = {city: MOCK_WEATHER_DATA.get(city, None) for city in requested_cities}
        conn.sendall(json.dumps(response).encode())
        conn.close()

# Client Code
def fetch_weather_from_server(cities):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 65432))
    client.sendall(json.dumps(cities).encode())
    data = client.recv(4096).decode()
    client.close()
    return json.loads(data)

# Main Function
def main():
    # Cities to monitor
    cities = ["London", "New York", "Sydney", "Mumbai", "Tokyo", "Unknown City"]

    # Fetch weather data from server
    weather_data = fetch_weather_from_server(cities)

    # Filter out None responses (cities not found)
    valid_weather_data = list(filter(None, weather_data.values()))

    # Display weather data
    print("Weather Data:")
    for city, data in weather_data.items():
        if data:
            print(f"{city}: {data['temperature']}°C, {data['weather']}")
        else:
            print(f"{city}: Data not available")

    # Functional Programming: Filter cities above a temperature threshold
    threshold = 20
    hot_cities = list(filter(lambda x: x["temperature"] > threshold, valid_weather_data))

    # Calculate average temperature using reduce
    average_temperature = reduce(lambda acc, x: acc + x["temperature"], valid_weather_data, 0) / len(valid_weather_data)

    print("\nCities with temperatures above 20°C:")
    for city in hot_cities:
        print(f"{city['temperature']}°C - {city['weather']}")

    print(f"\nAverage Temperature Across Monitored Cities: {average_temperature:.2f}°C")

# Run the server in a separate thread
import threading

server_thread = threading.Thread(target=weather_server, daemon=True)
server_thread.start()

# Run the main function
main()
