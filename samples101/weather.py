import json
import requests

def weather(location, apikey):
    url = 'https://samples.openweathermap.org/data/2.5/weather'
    query_params = {
        'q': location,
        'appid': apikey,
    }

    try:
        response = requests.get(url, params=query_params)
        response.raise_for_status()
        return(response.json()['weather'][0]['description'])

    except requests.exceptions.RequestException as e:
            return(e)
