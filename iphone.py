from tamrin.mobile import Mobile

class Iphone(Mobile):
    def __init__(self, name, price, voltage, screen_size, brand, serial):
        super().__init__(name, price, voltage, screen_size, brand)
        self.serial = serial
