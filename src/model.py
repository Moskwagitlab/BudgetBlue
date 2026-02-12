from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    amount: float
    category: str
    description: str
    type: str  
    date: str = datetime.now().strftime("%Y-%m-%d %H:%M")