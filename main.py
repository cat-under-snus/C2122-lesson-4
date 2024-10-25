class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}: ${self.price:.2f}"


class Order:
    def __init__(self):
        self.items = []
        self.status = "Pending"

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def set_status(self, status):
        self.status = status

    def get_order_summary(self):
        item_list = "\n".join([item.get_info() for item in self.items])
        return f"Order items:\n{item_list}\nTotal: ${self.total_price():.2f}\nStatus: {self.status}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.order = None

    def create_order(self):
        self.order = Order()

    def add_item_to_order(self, item):
        if not self.order:
            self.create_order()
        self.order.add_item(item)

    def view_order(self):
        if not self.order:
            return "No order placed."
        return self.order.get_order_summary()


customer = Customer("Alice")

coffee = Item("Coffee", 2.5)
sandwich = Item("Sandwich", 5.0)
cake = Item("Cake", 3.75)


customer.add_item_to_order(coffee)
customer.add_item_to_order(sandwich)
customer.add_item_to_order(cake)

print(customer.view_order())

customer.order.set_status("Completed")
print("\nUpdated Order Status:")
print(customer.view_order())