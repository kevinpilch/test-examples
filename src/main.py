import json
from src.utils.s3_client import S3Client

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

def process_costs_s3(
    s3_client: S3Client,
    input_bucket: str,
    input_key: str,
    output_bucket: str,
    output_key: str
) -> float:
    """
    Process costs from S3 and write results back to S3
    
    Args:
        s3_client: Initialized S3 client
        input_bucket: Source bucket name
        input_key: Source file key
        output_bucket: Destination bucket name
        output_key: Destination file key
    
    Returns:
        float: Total cost calculated
    """
    # Read and process
    file_contents = s3_client.read_from_s3(input_bucket, input_key)
    costs_dict = load_json(file_contents)
    costs = filter_costs(costs_dict)
    total_cost = calculate_total_cost(costs)
    
    # Write result back to S3
    result = {"total_cost": total_cost}
    s3_client.write_to_s3(
        output_bucket,
        output_key,
        json.dumps(result)
    )
    
    return total_cost

def improved_get_costs_from_file(path: str) -> float:
    file_contents = read_file(path)
    costs_dict = load_json(file_contents)
    costs = filter_costs(costs_dict)
    total_cost = calculate_total_cost(costs)
    return total_cost

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

# Now, the code is more modular and easier to understand.
# Each function has a single responsibility.
# We can easily test this.
