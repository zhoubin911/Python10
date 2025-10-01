from tamrin.product import Product

class Non_Electrical(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

