from api import NBAAPI
from processing import SalaryProcessor
from visualization import SalaryVisualizer
def main():
    # Initialize API and fetch data
    nba_api = NBAAPI("https://api.example.com")  # Give an API
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
