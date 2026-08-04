# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: RentTracker
import unittest


class TestRentTracker(unittest.TestCase):
    def test_rent_create(self):
        from rent_tracker import RentItem, Customer
        cust = Customer("Ivan", "ivan@example.com")
        item = RentItem(id=1, name="Drill", owner=cust)
        item.status = "rented"
        self.assertEqual(item.owner, cust)

    def test_rent_due_date(self):
        from rent_tracker import RentItem, Customer
        cust = Customer("Maria", "maria@example.com")
        item = RentItem(id=2, name="Camera", owner=cust)
        item.status = "rented"
        due = item.get_due_date(days=14)
        self.assertIsInstance(due, datetime.date)

    def test_rent_history(self):
        from rent_tracker import RentItem, Customer, HistoryEntry
        cust = Customer("Oleg", "oleg@example.com")
        item = RentItem(id=3, name="Bike", owner=cust)
        item.status = "rented"
        history = item.get_history()
        self.assertIsInstance(history, list)

    def test_customer_name(self):
        from rent_tracker import Customer
        c = Customer("Anna", "anna@test.com")
        self.assertEqual(c.name, "Anna")


if __name__ == "__main__":
    unittest.main()
