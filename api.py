# Import package 
import requests

# Encapsulate setup for the NBA API
class Nba_api_config:

    # Initialize API headers and any default configurations
    def __init__(self):
        self.base_url = 'https://stats.nba.com/stats'
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'x-nba-stats-token': 'true',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/79.0.3945.130 Safari/537.36',
            'x-nba-stats-origin': 'stats',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Referer': 'https://stats.nba.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }

    # Retrieve API headers
    def get_headers(self):

        return self.headers

    def fetch_data(self, endpoint):
        """
        Fetches data from specified API endpoint.
        :param endpoint: API endpoint to fetch data from.
        :return: JSON data if successful, None if otherwise. 
        """
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers) 
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
