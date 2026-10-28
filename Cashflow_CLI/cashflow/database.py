# Importing libs for file creation and file-to-path storage
import json
from pathlib import Path
from datetime import datetime

# Defining where the JSON file will live
DATA_FILE = Path("finance.json")

def save_data(data: dict):
    """Takes a dictionary and writes it to finance.json"""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)

def load_data():
    """Loads financial data from json file and creates default structure if doesn't exist"""
    # Default structure creature
    if not DATA_FILE.exists():
        default_data = {"transactions": [], "budget": {}, "goals": []}
        save_data(default_data)
        return default_data
    else:
        try:
            with open(DATA_FILE, "r") as file:
                json.load(file)
        except json.JSONDecodeError:
            print("[Warning] finance.json was corrupted. Reseting data structure.")
            return {"transactions": [], "budget": {}, "goals": []}

def add_transaction(amount: float, t_type: str, category: str, description: str):
    """Creates a financial dictionary and saves it to finance.json"""
    data = load_data()

    # Creating id based on number of transactions
    new_id = str(len(data["transactions"]) + 1)

    # Building transaction dictionary
    transaction = {
        "id": new_id,
        "date": datetime.now().strftime("%Y-%m-%D %H:%M"),
        "type": t_type.lower(),    # income or expense
        "category": category,
        "amount": float(amount),
        "description": description
    }

    # Adding to list and saving back to file
    data["transactions"].append(transaction)
    save_data(data)
    return  transaction