import typer
from rich.console import Console
from rich.table import Table
from cashflow.database import(
    add_transaction,
    set_budget,
    set_goal,
    goal_contribution,
    load_data
)

# Initializing Typer app and Rich console
app = typer.Typer(help="Cashflow CLI - Manage your finances with ease")
console = Console()

@app.command("transaction")
def add_transaction_cli(
    amount: float = typer.Option(..., "--amount", "-a", help="Amount of the transaction"),
    t_type: str = typer.Option(..., "--t_type", "-t", help="Type of transaction: income or expense"),
    category: str = typer.Option(..., "--category", "-c", help="Category of the transaction"),
    description: str = typer.Option(..., "--description", "-d", help="Description of the transaction")
):
    """Add a new financial transaction"""
    transaction = add_transaction(amount, t_type, category, description)
    console.print(f"[green]Transaction added successfully![/green]\n [bold]{transaction}[/bold]")

@app.command("budget")
def set_budget_cli(
   category: str = typer.Option(..., "--category", "-c", help="Category of the transaction"),
   limit: float = typer.Option(..., "--limit", "-l", help="Limit amount")
):
   """Sets a monthly spending cap for a specific category"""
   set_budget(category, limit)
   console.print(f"[green]Budget set successfully![/green]\n [bold]Category: {category}, Limit: {limit}[/bold]")
 
@app.command("goal")
def set_goal_cli(
   name: str = typer.Option(..., "--name", "-n", help="Name of the goal"),
   target_amt: float = typer.Option(..., "--target", "-T", help="Target amount for the goal")
):
   """Sets a financial target"""
   set_goal(name, target_amt)
   console.print(f"[green]Goal set successfully![/green]\n [bold]Goal: {name}, Target: {target_amt}[/bold]")

@app.command("contribution")
def goal_contribution_cli(
   name: str = typer.Option(..., "--name", "-n", help="Name of the goal"),
   amount: float = typer.Option(..., "--amount", "-a", help="Amount to contribute to the goal")
):
   """Add money to existing goal"""
   goal = goal_contribution(name, amount)
   if goal:
        console.print(f"[green]Contribution added successfully![/green]\n [bold]{goal}[/bold]")
        if goal["status"] == "Complete":
            console.print(f"[blue]Congratulations! You've completed the goal: {goal['name']}[/blue]")
        if goal["status"] == "Incomplete":
            console.print(f"[yellow]Current amount: {goal['current_amount']} / Target: {goal['target']}[/yellow]")
   else:
      console.print(f"[red]Goal not found.[/red]")
     
   
   

if __name__ == "__main__":
  app()