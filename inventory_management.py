class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item, quantity, price):
        if item in self.stock:
            self.stock[item]['quantity'] += quantity
        else:
            self.stock[item] = {'quantity': quantity, 'price': price}

    def update_stock(self, item, quantity):
        if item in self.stock:
            self.stock[item]['quantity'] = quantity
        else:
            print(f"Item {item} not found in inventory.")

    def update_price(self, item, price):
        if item in self.stock:
            self.stock[item]['price'] = price
        else:
            print(f"Item {item} not found in inventory.")

    def calculate_total(self):
        total = 0
        for item in self.stock:
            total += self.stock[item]['quantity'] * self.stock[item]['price']
        return total

    def display_stock(self):
        for item in self.stock:
            print(f"Item: {item}, Quantity: {self.stock[item]['quantity']}, Price: {self.stock[item]['price']}")

# Example usage
inventory = Inventory()
inventory.add_stock('apple', 10, 2)
inventory.add_stock('banana', 5, 1.5)
inventory.update_stock('apple', 15)
inventory.update_price('banana', 1.8)
inventory.display_stock()
print(f"Total inventory value: {inventory.calculate_total()}")
