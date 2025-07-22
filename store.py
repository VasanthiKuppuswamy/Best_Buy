class Store:


    def __init__(self, productlist):
        self.products = productlist

    def add_product(self, product):
        self.products.append(product)
    def remove_product(self, product):
        self.products.remove(product)
    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity
    def get_all_products(self):
        total_products = []
        for product in self.products:
            if product.is_active():
                total_products.append(product)
        return total_products
    def order(self, shopping_list):
        total_price = 0
        for product , quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price






