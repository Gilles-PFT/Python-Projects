# CashFlow CLI

A persistent, terminal-based personal finance manager built with Python, **Typer**, and **Rich**. CashFlow CLI lets you log income and expenses, set monthly category spending caps, and track savings goals directly from your command line, storing all records in a local JSON database.

---

## Features

- **Transaction Logging:** Record income and expenses with automatic timestamps (`YYYY-MM-DD HH:MM`), sequential IDs, categories, and descriptions.
- **Monthly Category Budgets:** Define and update spending limits per category to organize monthly expenses.
- **Savings Goal Tracking:** Create financial targets, make incremental contributions (case-insensitive matching), and automatically mark goals as `Complete` once reached.
- **Reliable Local Persistence:** Anchors `finance.json` to the project root using `pathlib` (`Path(__file__).resolve().parent.parent`) so commands read and write to the same file regardless of your terminal's working directory.
- **Formatted Terminal Output:** Clean, color-coded terminal feedback and tables powered by `rich`.

---

## Tech Stack

- **Language:** Python 3.12+
- **CLI Framework:** [Typer]
- **Terminal Formatting:** [Rich]
- **Standard Library:** `json`, `pathlib`, `datetime`

---

## Project Structure

```text
Cashflow_CLI/
├── cashflow/
│   ├── __init__.py      # Marks cashflow as a Python package
│   ├── cli.py           # Typer CLI commands and Rich terminal output
│   └── database.py      # CRUD operations and JSON persistence
├── finance.json         # Auto-generated local JSON database (ignored in Git)
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation 
```
---

## Installation and setup

### 1. Clone the repository
```bash
git clone [https://github.com/Gilles-PFT/Python-Projects.git](https://github.com/Gilles-PFT/Python-Projects.git)
cd Python-Projects/Cashflow_CLI
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install typer rich
```
---

## Usage

Run all commands from the `Cashflow_CLI` root folder using `python -m cashflow.cli`

### Log a Transaction (transaction)

Record an income entry or an expense:
```bash
# Log income
python -m cashflow.cli transaction -a 150000 -t income -c salary -d "Monthly salary"

# Log an expense
python -m cashflow.cli transaction -a 4500 -t expense -c food -d "Weekly groceries"
```

| Option | Short | Description |
| :--- | :--- | :--- |
|`--amount`|`-a`|Transaction amount (`float`)|
|`--t-type`|`-t`|Transaction type (`income` or `expense`)|
|`--category`|`-c`|Income or spending category|
|`--description`|`-d`|Brief description of the transaction|

### Set a Monthly Budget (budget)

Create or update a monthly spending limit for a category:
```bash
python -m cashflow.cli budget -c food -l 25000
```

| Option | Short | Description |
| :--- | :--- | :--- |
|`--category`|`-c`|Category name|
|`--limit`|`-l`|Monthly spending cap (`float`)|

### Set a saving goal (goal)

Define a new savings target:
```bash
python -m cashflow.cli set-goal -n "Trip" -t 60000
```

| Option | Short | Description |
| :--- | :--- | :--- |
|`--name`|`-n`|Name of the savings goal|
|`--target`|`-T`|Target amount to save (`float`)|

### Contibute to a goal (contribute)

Add funds towards an existing saving goal:
```bash
python -m cashflow.cli contribution -n "Trip" -a 15000
```

| Option | Short | Description |
| :--- | :--- | :--- |
|`--name`|`-n`|Name of the existing goal|
|`--amount`|`-a`|Amount to contribute (`float`)|


## Data storage (finance.json)
On first execution, database.py automatically creates finance.json in the Cashflow_CLI/ root directory with the following structure:

```bash
{
  "transactions": [
    {
      "id": "1",
      "date": "2026-11-16 23:40",
      "type": "income",
      "category": "salary",
      "amount": 150000.0,
      "description": "Monthly salary"
    }
  ],
  "budgets": {
    "food": 25000.0
  },
  "goals": [
    {
      "name": "Trip",
      "target": 60000.0,
      "current_amount": 15000.0,
      "status": "Incomplete"
    }
  ]
}
```




