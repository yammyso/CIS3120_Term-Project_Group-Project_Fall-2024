import requests
class NBAAPI:
    def __init__(self, base_url):
        """
        Initializes the NBA API class with the base URL.
        
        :param base_url: The URL to the NBA player data API.
        """
        self.base_url = base_url

    def fetch_data(self, endpoint):
        """
        Fetches data from the specified API endpoint.
        :param endpoint: API endpoint to fetch data from.
        :return: JSON data if successful, None otherwise.
        """
        try:
            response = requests.get(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
