class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running laptop: {self.brand}'


class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dual_sim}'


my_phone = Phone('iphone', 120000, 'silver', 'china', True)
print(my_phone)
