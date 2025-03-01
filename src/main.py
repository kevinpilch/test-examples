import json

# This function does too many things.
def get_costs_from_file(path: str) -> float:
    """
    Get costs from a JSON file.

    :param path: Path to the JSON file.
    :return: Total cost.

    """
    with open(path, 'r') as file:
        file_contents = file.read()
    costs_dict = json.loads(file_contents)
    costs = []
    for obj in costs_dict:
        if obj.get('type') == 'cost':
            cost = obj.get('cost')
            print(f'Cost: {cost}')
            costs.append(cost)
    total_cost = sum(costs)
    return total_cost



# Let's refactor this function to make it more modular.

def read_file(path: str) -> str:
    with open(path, 'r') as file:
        file_contents = file.read()
    return file_contents

def load_json(file_contents: str) -> list[dict]:
    return json.loads(file_contents)

def filter_costs(costs_dict: list[dict]) -> list:
    costs = []
    for obj in costs_dict:
        if obj.get('type') == 'cost':
            cost = obj.get('cost')
            costs.append(cost)
    return costs

def calculate_total_cost(costs: list) -> float:
    return sum(costs)

def improved_get_costs_from_file(path: str) -> float:
    file_contents = read_file(path)
    costs_dict = load_json(file_contents)
    costs = filter_costs(costs_dict)
    total_cost = calculate_total_cost(costs)
    return total_cost

# Now, the code is more modular and easier to understand.
# Each function has a single responsibility.
# We can easily test this.
