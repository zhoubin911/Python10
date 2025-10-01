from tamrin.non_electrical import Non_Electrical

class Furniture(Non_Electrical):
    def __init__(self, name, price, weight, capacity):
        super().__init__(name, price, weight)
        self.capacity = capacity

