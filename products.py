class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    def activate(self):
        self.active = True
    def deactivate(self):
        self.active = False
    def is_active(self):
        return self.active
    def show(self):
        return f"{self.name}, {self.price}, {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity > self.quantity:
            raise ValueError("The required quantity is not available")
        if quantity <= 0:
            raise ValueError("Quantity needs to be a positive number.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity




if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())