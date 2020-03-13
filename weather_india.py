import requests, json, time
import config

# Function to load the json file containing the details of cities,
# and to create a dictionary of Indian cities with their names as keys and
# IDs as values.
def setup(city_code):
    with open('city_list.json', 'r', encoding = 'utf8') as city_list:
        cities = json.load(city_list)
    for city in cities:
        if city['country'] == 'IN':
            city_code[city['name'].lower()] = str(city['id'])

# Function to fetch the response to the HTTP request to get the weather information of the city,
# and to return the status code and json-encoded content of the reponse, if any.
def fetch_data(city_id):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?id='
    # Refer to README.md for instructions on API key generation and creation of configuration file
    app_id = config.api_key
    url = base_url + city_id + '&appid=' + app_id
    response = requests.get(url)
    return response.status_code, response.json()

# Main (Driver) function to get the user input, store relevant weather information,
# and display the weather information for the city.
def main():
    city_code, city_id = dict(), None
    setup(city_code)
    print('\nWEATHER INDIA\n')
    city_name = input('Enter an Indian city\'s name: ').lower()
    # Check if the user-entered city is present in the given list of cities, and to assign its ID
    if city_name in city_code:
        city_id = city_code[city_name]
    if city_id:
        status_code, data = fetch_data(city_id)
        if status_code == 200:
            conv = 273.15   # Conversion factor to convert temp. from K to C scale
            name = data['name']
            weather = {
            'main': data['weather'][0]['main'],
            'desc': data['weather'][0]['description']
            }
            temp = {
            'cur_temp': round(data['main']['temp'] - conv, 2),
            'min_temp': round(data['main']['temp_min'] - conv, 2),
            'max_temp': round(data['main']['temp_max'] - conv, 2),
            'feels_like': round(data['main']['feels_like'] - conv, 2)
            }
            humidity = data['main']['humidity']
            # Wind speed multiplied by 3.6 to convert meter/sec to km/hr
            wind_speed = round(data['wind']['speed'] * 3.6, 2)
            cloudiness = data['clouds']['all']
            # Conversion of Unix Timestamp to easily understandable date and time
            sun_time = {
            'sunrise': time.ctime(data['sys']['sunrise']).split(),
            'sunset': time.ctime(data['sys']['sunset']).split()
            }
            print(f'\nCURRENT WEATHER INFORMATION for {name.upper()}:\n')
            print('Weather Condition: ' + weather['main'] + ' (' \
            + weather['desc'] + ')')
            print('Current Temperature : ' + str(temp['cur_temp']) + ' C')
            print('Current Minimum Temperature : ' \
            + str(temp['min_temp']) + ' C')
            print('Current Maximum Temperature : ' \
            + str(temp['max_temp']) + ' C')
            print('\'Feels Like\' Temperature : ' \
            + str(temp['feels_like']) + ' C')
            print(f'Humidity: {humidity} %')
            print(f'Wind Speed: {wind_speed} km/hr')
            print(f'Cloudiness: {cloudiness} %')
            sunrise, sunset = sun_time['sunrise'], sun_time['sunset']
            print('Sunrise Time:  ' + sunrise[2] + ' ' + sunrise[1] + ' ' \
            + sunrise[-1] + ' (' + sunrise[0] + ') ' + sunrise[-2] + ' IST (local time)')
            print('Sunset Time:  ' + sunset[2] + ' ' + sunset[1] + ' ' \
            + sunset[-1] + ' (' + sunset[0] + ') ' + sunset[-2] + ' IST (local time)\n')
        else:
            print('\nUnsuccessful HTTP request :(')
    else:
        print(f'\n{city_name.title()} is not currently present in our list of Indian cities :(\n')



if __name__ == '__main__':
    main()
