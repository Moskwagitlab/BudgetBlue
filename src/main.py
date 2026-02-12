import typer
from .model import Transaction
from .database import save_transaction, load_transactions
from .ui import print_transactions, print_banner, print_success, console

app = typer.Typer()

#transakcja
@app.command()
def add(amount: float, category: str, description: str, type: str = "EXPENSE"):
    """Dodaj nową transakcję"""
    t = Transaction(amount, category, description, type.upper())
    save_transaction(t)
    print_success(f"Dodano: {description} ({amount} PLN)")

#wyswietlanie
@app.command()
def list():
    """Wyświetl niebieską tabelę"""
    print_banner()
    data = load_transactions()
    print_transactions(data)

if __name__ == "__main__":
    app()