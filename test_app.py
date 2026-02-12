import unittest
from src.model import Transaction

class TestBudgetBlue(unittest.TestCase):
    def test_create_transaction(self):
        t = Transaction(100, "Test", "Opis", "INCOME")
        self.assertEqual(t.amount, 100)
        self.assertEqual(t.type, "INCOME")
        self.assertEqual(t.category, "Test")

if __name__ == '__main__':
    unittest.main()