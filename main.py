from api import NBAAPI
from processing import SalaryProcessor
from visualization import SalaryVisualizer

def main():
    # Initialize API and fetch data
    nba_api = NBAAPI("https://api.example.com") 
    data = nba_api.fetch_data("players_salaries")  # Replace with the actual API endpoint

    if not data or not isinstance(data, list):
        print("Error: No valid data fetched from the API.")
        return
        
    # Process the data
    processor = SalaryProcessor(data)
        
    # Display the highest paid player
    highest_paid_player = processor.get_highest_paid_player()
    if highest_paid_playe: 
        print(f"The highest paid player is {highest_paid_player.name} with a salary of ${highest_paid_player.salary}.")
    else: 
        print("No player data available to determine the highest paid player.")

    # Display the average salary
    average_salary = processor.get_average_salary()
    if average_salary is not None: 
        print(f"The average salary of NBA players is ${average_salary:,.2f}.")
    else: 
        print("Not enough data to calculate the average salary.")

    # Visualize the salary distribution
    if hassattr(processor, 'players') and processor.players:
        visualizer = SalaryVisualizer(processor.players)
        visualizer.visualize_salaries()
        visualizer.visualize_salary_distribution()
    else: 
        print("No player data available for visualization.") 
        
if __name__ == "__main__":
    main()


