# Weather-India

* [__weather_india.py__](weather_india.py) uses the __Current Weather Data__ from the [__Weather API__](https://openweathermap.org/api) provided by [__OpenWeatherMap__](https://openweathermap.org/) to provide current weather information for Indian cities.

* The user has to provide an Indian city's name to see the current weather information for the same city, if that city is present in the list of Indian cities obtained from the API.

* Data for the following weather parameters are shown as the result:
  * Current weather condition with description
  * Current temperature (Celsius scale)
  * Current minimum temperature (Celsius scale)
  * Current maximum temperature (Celsius scale)
  * 'Feels like' temperature (Celsius scale)
  * Humidity percentage
  * Wind speed (km/hr)
  * Cloudiness percentage
  * Sunrise time (UTC)
  * Sunset time (UTC)
  
### Modules Used

* [*__requests__*](https://pypi.org/project/requests/)
  * To make HTTP request to the API and fetch the response (current weather data for the city - using the city's ID and API key)
  * To return json-encoded content of the response (if any)
  
* [*__json__*](https://docs.python.org/3.8/library/json.html)
  * To load the json file containing the list of all the cities and their data (provided by the API) into a Python object
  
* [*__time__*](https://docs.python.org/3.8/library/time.html)
  * To convert the sunrise and sunset times given as Unix Timestamps into easily understandable date and time format strings
