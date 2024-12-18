from api import NBAAPI
from processing import SalaryProcessor
from visualization import SalaryVisualizer

class PositionFilter:
    def __init__(self, players):
        self.players = players

    def filter_by_position(self, position):
        return [player for player in self.players if player.position.lower() == position.lower()]

def main():
    # Initialize API and fetch data
    nba_api = NBAAPI("https://github.com/swar/nba_api/tree/master")  
    data = nba_api.fetch_data("players_salaries") 

    if data:
        # Process the data
        processor = SalaryProcessor(data)

        # Display the highest paid player
        highest_paid_player = processor.get_highest_paid_player()
        print(f"The highest paid player is {highest_paid_player.name} with a salary of ${highest_paid_player.salary}.")

        # Display the average salary
        average_salary = processor.get_average_salary()
        print(f"The average salary of NBA players is ${average_salary:,.2f}.")

        # Filter players by position
        position_filter = PositionFilter(processor.players)
        position = input("Enter a position to filter by (e.g., Guard, Forward, Center): ")
        filtered_players = position_filter.filter_by_position(position)

        print(f"Players in the {position} position:")
        for player in filtered_players:
            print(f"{player.name}: ${player.salary}")

        # Visualize the salary distribution
        visualizer = SalaryVisualizer(processor.players)
        visualizer.visualize_salaries()
        visualizer.visualize_salary_distribution()

if __name__ == "__main__":
    main()
