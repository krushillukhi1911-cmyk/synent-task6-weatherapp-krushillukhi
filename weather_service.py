import requests
from requests.exceptions import RequestException, Timeout

class WeatherService:
    BASE_URL = 'https://api.openweathermap.org/data/2.5/'
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def get_current_weather(self, city):
        """Fetch current weather for a given city."""
        if not self.api_key:
            return {'error': 'API Key is missing.'}
            
        url = f"{self.BASE_URL}weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric' # default to Celsius
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 404:
                return {'error': f'City "{city}" not found.', 'status': 404}
            if response.status_code == 429:
                return {'error': 'API rate limit exceeded. Please try again later.', 'status': 429}
            response.raise_for_status()
            return response.json()
        except Timeout:
            return {'error': 'Request timed out. Please check your connection and try again.', 'status': 408}
        except RequestException as e:
            return {'error': f'Network error occurred: {str(e)}', 'status': 500}
        except Exception as e:
             return {'error': f'An unexpected error occurred: {str(e)}', 'status': 500}

    def get_forecast(self, city):
        """Fetch 5-day forecast for a given city."""
        if not self.api_key:
            return {'error': 'API Key is missing.'}
            
        url = f"{self.BASE_URL}forecast"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 404:
                return {'error': f'City "{city}" not found.', 'status': 404}
            if response.status_code == 429:
                return {'error': 'API rate limit exceeded. Please try again later.', 'status': 429}
            response.raise_for_status()
            return response.json()
        except Timeout:
            return {'error': 'Request timed out. Please check your connection and try again.', 'status': 408}
        except RequestException as e:
            return {'error': f'Network error occurred: {str(e)}', 'status': 500}
        except Exception as e:
             return {'error': f'An unexpected error occurred: {str(e)}', 'status': 500}
