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
