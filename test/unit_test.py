from src.main import read_file, load_json, filter_costs, calculate_total_cost, improved_get_costs_from_file

def test_read_file():
    """Test reading file contents"""
    path = 'test/data/cost_export.json'
    file_contents = read_file(path)
    assert isinstance(file_contents, str)
    assert len(file_contents) > 0

def test_load_json():
    """Test loading JSON from string"""
    file_contents = '[{"id": 1, "type": "expense", "amount": "$125.00", "date": "2025-01-01", "description": "Office Supplies"}]'
    costs_dict = load_json(file_contents)
    assert isinstance(costs_dict, list)
    assert len(costs_dict) == 1
    assert costs_dict[0]['id'] == 1

def test_filter_costs():
    """Test filtering costs from JSON data"""
    costs_dict = [
        {"id": 1, "type": "expense", "amount": "$125.00", "date": "2025-01-01", "description": "Office Supplies"},
        {"id": 2, "type": "expense", "amount": "$50.00", "date": "2025-01-02", "description": "Gas"},
        {"id": 3, "type": "sale", "amount": "$500.00", "date": "2025-01-03", "description": "Sale of Goods"}
    ]
    costs = filter_costs(costs_dict)
    assert isinstance(costs, list)
    assert len(costs) == 0  # No 'cost' type in the provided data

def test_calculate_total_cost():
    """Test calculating total cost"""
    costs = [125.00, 50.00]
    total_cost = calculate_total_cost(costs)
    assert total_cost == 175.00

def test_improved_get_costs_from_file():
    """Test the improved get costs from file function"""
    path = 'test/data/cost_export.json'
    total_cost = improved_get_costs_from_file(path)
    assert total_cost == 0.00  # No 'cost' type in the provided data