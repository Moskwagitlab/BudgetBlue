import json
import os
from typing import List
from .model import Transaction

DB_FILE = 'finance_db.json'

def load_transactions() -> List[dict]:
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_transaction(t: Transaction):
    data = load_transactions()
    data.append(t.__dict__)
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)