# backend/data_access/database_connector.py
def get_policy_data():
    """
    Simulates fetching raw policy data from a database.
    In a real application, this would connect to a database (SQL, NoSQL).
    """
    # Return dummy policy data
    return [
        {"policy_id": "P001", "type": "Auto", "region": "North America", "insured_value": 1500000, "premium": 1200},
        {"policy_id": "P002", "type": "Home", "region": "Florida", "insured_value": 2500000, "premium": 2500},
        {"policy_id": "P003", "type": "Life", "region": "Europe", "insured_value": 800000, "premium": 800},
        {"policy_id": "P004", "type": "Commercial", "region": "Asia", "insured_value": 3000000, "premium": 3500},
        {"policy_id": "P005", "type": "Auto", "region": "North America", "insured_value": 1200000, "premium": 1000},
        {"policy_id": "P006", "type": "Home", "region": "California", "insured_value": 2000000, "premium": 2000},
        {"policy_id": "P007", "type": "Life", "region": "South America", "insured_value": 700000, "premium": 700},
        {"policy_id": "P008", "type": "Commercial", "region": "Europe", "insured_value": 4000000, "premium": 4000},
        {"policy_id": "P009", "type": "Health", "region": "North America", "insured_value": 1800000, "premium": 1800},
        {"policy_id": "P010", "type": "Health", "region": "Asia", "insured_value": 1000000, "premium": 1000},
    ]