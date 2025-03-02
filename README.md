# Test Automation with Python and GitHub Actions

This project demonstrates best practices for writing testable Python code and implementing automated testing using pytest. 
It showcases code refactoring for better testability and setting up continuous integration with GitHub Actions.

## Project Overview

The project includes a simple cost calculation program that demonstrates:
- Single Responsibility Principle in function design
- Unit testing with pytest
- Code refactoring for better testability
- Continuous Integration setup with GitHub Actions

The program reads a JSON file containing cost data and calculates the total cost.

## Project Setup

To set up this project using Python 3.11, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   
2. **Create a virtual environment:**  
    ```sh
    python3.11 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

3. **Install dependencies:**  
    ```sh
    pip install -r requirements.txt

## Refactoring Explanation

You can find the relevant code in the `src.main` module.

The `get_costs_from_file` function in `src.main` was refactored to improve modularity and testability. 
The original function performed multiple tasks, making it difficult to test and maintain. 
The refactored version breaks down the functionality into smaller, single-responsibility functions:

- `read_file(path: str) -> str`: Reads the contents of a file.
- `load_json(file_contents: str) -> list[dict]`: Parses a JSON string into a list of dictionaries.
- `filter_costs(costs_dict: list[dict]) -> list`: Filters the costs from the JSON data.
- `calculate_total_cost(costs: list) -> float`: Calculates the total cost from a list of costs.
- `improved_get_costs_from_file(path: str) -> float`: Combines the above functions to achieve the original functionality.


## Running Tests
To run the tests, use the following command:
```sh
pytest 
```

## Continuous Integration with GitHub Actions
A GitHub Actions pipeline is defined in `.github/workflows/unit_tests.yml`. 
This pipeline is configured to run the unit tests automatically. 
The pipeline is triggered on the following events:
- `pull_request` to all branches other than `main`

To run the pipeline in your own GitHub repository, you need to:
- Create a public repository on GitHub
- Push the code to the `main` branch of your repository
- Create a new branch locally and create some changes
- Push the new branch to your GitHub repository and open a pull request
