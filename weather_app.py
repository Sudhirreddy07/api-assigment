import requests


api = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    try:
        response = requests.get(api)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_temperature(weather_data, date_time):
    for forecast in weather_data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['main']['temp']
    return None

def get_wind_speed(weather_data, date_time):
    for forecast in weather_data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['wind']['speed']
    return None

def get_pressure(weather_data, date_time):
    for forecast in weather_data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['main']['pressure']
    return None

def main():
    weather_data = get_weather_data()
    if not weather_data:
        return

    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date_time = input("Enter date and time : ")
            temperature = get_temperature(weather_data, date_time)
            if temperature is not None:
                print(f"Temperature at {date_time}: {temperature} K")
            else:
                print("Data not found for the specified date and time.")

        elif choice == '2':
            date_time = input("Enter date and time : ")
            wind_speed = get_wind_speed(weather_data, date_time)
            if wind_speed is not None:
                print(f"Wind Speed at {date_time}: {wind_speed} m/s")
            else:
                print("Data not found for the specified date and time.")

        elif choice == '3':
            date_time = input("Enter date and time : ")
            pressure = get_pressure(weather_data, date_time)
            if pressure is not None:
                print(f"Pressure at {date_time}: {pressure} hPa")
            else:
                print("Data not found for the specified date and time.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
