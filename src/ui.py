from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.theme import Theme
from rich import box

# Definiujemy "Pastel Blue Theme"
custom_theme = Theme({
    "info": "sky_blue3",
    "warning": "plum2",      # Pastelowy różowy dla ostrzeżeń/wydatków
    "success": "spring_green2", # Miętowy dla sukcesów
    "header": "dodger_blue2 bold",
    "border": "sky_blue3"
})

console = Console(theme=custom_theme)

def print_banner():
    # niebieski panel
    console.print(Panel(
        "[header]💎  BudgetBlue Manager  💎[/header]", 
        expand=False, 
        border_style="border",
        padding=(1, 4)
    ))

def print_transactions(transactions):
    if not transactions:
        console.print(Panel("☁️  Brak transakcji w bazie! Dodaj coś.", border_style="warning"))
        return

    # Tworzymy tabelkę w stylu "Rounded" (zaokrąglone rogi)
    table = Table(title="[header]Historia Operacji[/header]", box=box.ROUNDED, border_style="border")
    
    table.add_column("Data 📅", style="dim cyan", no_wrap=True)
    table.add_column("Typ", style="white")
    table.add_column("Kategoria 🏷️", style="info")
    table.add_column("Opis 📝", style="white")
    table.add_column("Kwota 💰", justify="right")

    total = 0
    for t in transactions:
        amount = t['amount']
        if t['type'] == 'EXPENSE':
            # Styl dla wydatku (różowy pastel) .
            color_tag = "warning"
            type_icon = "📉"
            total -= amount
            amount_str = f"-{amount:.2f} PLN"
        else:
            # Styl dla przychodu (miętowy/zielony)
            color_tag = "success"
            type_icon = "📈"
            total += amount
            amount_str = f"+{amount:.2f} PLN"
            
        table.add_row(
            t['date'], 
            f"{type_icon} {t['type']}", 
            t['category'], 
            t['description'], 
            f"[{color_tag}]{amount_str}[/{color_tag}]"
        )

    console.print(table)
    
    # Podsumowanie [stan konta]
    saldo_color = "success" if total >= 0 else "warning"
    console.print(Panel(
        f"Stan konta: [{saldo_color} bold]{total:.2f} PLN[/{saldo_color} bold]", 
        title="[header]Podsumowanie[/header]", 
        border_style="border",
        expand=False
    ))

def print_success(msg):
    console.print(f"[success]✨ {msg} ✨[/success]")