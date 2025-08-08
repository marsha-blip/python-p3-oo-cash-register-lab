class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0.0

    def add_item(self, title, price, quantity=1):
        price = float(price)
        quantity = int(quantity)
        item_total = price * quantity
        self.total += item_total
        self.items.extend([title] * quantity)
        self.last_transaction_amount = item_total
        return self.total

    def _format_total(self, total):
        """Format total: integer if whole number, otherwise two decimals."""
        t = float(total)
        if t.is_integer():
            return str(int(t))
        else:
            return f"{t:.2f}"

    def apply_discount(self):
        """
        Apply the instance discount to self.total.

        - If discount == 0: print and return the 'no discount' message.
        - If discount > 0: update self.total, print and return the success message.
        """
        if not self.discount:  # discount == 0
            message = "There is no discount to apply."
            print(message)
            return message + "\n"

        # compute discounted total and update self.total
        self.total = self.total * (100 - self.discount) / 100.0

        total_str = self._format_total(self.total)
        message = f"After the discount, the total comes to ${total_str}."
        print(message)
        return message + "\n"

    def get_items(self):
        return self.items

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        if self.total < 0:
            self.total = 0.0
        return self.total




