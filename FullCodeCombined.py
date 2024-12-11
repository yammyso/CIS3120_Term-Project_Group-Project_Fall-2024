import requests
import matplotlib.pyplot as plt
import seaborn as sns
# Define the Player class
class Player:
    def __init__(self, name, team, salary):
        """
        Initializes an NBA player object.
        :param name: Player's name.
        :param team: Player's team.
        :param salary: Player's salary.
        """
        self.name = name
        self.team = team
        self.salary = salary

    def __str__(self):
        """
        Returns a string representation of the player.
        """
        return f"{self.name} plays for {self.team} and earns ${self.salary} annually."

# Define the SalaryProcessor class
class SalaryProcessor:
    def __init__(self, data):
        """
        Initializes the SalaryProcessor with the player data.
        
        :param data: List of player data (dict).
        """
        self.players = [Player(player['name'], player['team'], player['salary']) for player in data]

    def get_highest_paid_player(self):
        """
        Returns the highest paid player.
        
        :return: Player object of the highest paid player.
        """
        return max(self.players, key=lambda player: player.salary)

    def get_players_by_team(self, team_name):
        """
        Returns all players from a specific team.
        
        :param team_name: Name of the team.
        :return: List of Player objects from the team.
        """
        return [player for player in self.players if player.team == team_name]

    def get_average_salary(self):
        """
        Returns the average salary of all players.
        
        :return: Average salary.
        """
        total_salary = sum(player.salary for player in self.players)
        return total_salary / len(self.players) if self.players else 0

# Define the SalaryVisualizer class
class SalaryVisualizer:
    def __init__(self, players):
        """
        Initializes the SalaryVisualizer with a list of players.
        
        :param players: List of Player objects.
        """
        self.players = players

    def visualize_salaries(self):
        """
        Creates a bar chart of the NBA players' salaries.
        """
        player_names = [player.name for player in self.players]
        player_salaries = [player.salary for player in self.players]
        plt.figure(figsize=(12, 6))
        sns.barplot(x=player_names, y=player_salaries)
        plt.xticks(rotation=90)
        plt.title("NBA Player Salaries")
        plt.xlabel("Player Name")
        plt.ylabel("Salary (USD)")
        plt.tight_layout()
        plt.show()

    def visualize_salary_distribution(self):
        """
        Creates a histogram of the NBA player salaries.
        """
        salaries = [player.salary for player in self.players]
        plt.figure(figsize=(10, 6))
        sns.histplot(salaries, kde=True, bins=20)
        plt.title("Salary Distribution of NBA Players")
        plt.xlabel("Salary (USD)")
        plt.ylabel("Frequency")
        plt.show()

# Define the NBAAPI class
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
# Main program logic
def main():
    # Initialize API and fetch data
    nba_api = NBAAPI("https://api.example.com")  # Replace with the actual API
    data = nba_api.fetch_data("players_salaries")  # Replace with the actual API endpoint

    if data:
        # Process the data
        processor = SalaryProcessor(data)

        # Display the highest paid player
        highest_paid_player = processor.get_highest_paid_player()
        print(f"The highest paid player is {highest_paid_player.name} with a salary of ${highest_paid_player.salary}.")

        # Display the average salary
        average_salary = processor.get_average_salary()
        print(f"The average salary of NBA players is ${average_salary:,.2f}.")

        # Visualize the salary distribution
        visualizer = SalaryVisualizer(processor.players)
        visualizer.visualize_salaries()
        visualizer.visualize_salary_distribution()
if __name__ == "__main__":
    main()
