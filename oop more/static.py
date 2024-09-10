class Shopping:
    cart = []  # class attribute #static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = 'jamuna city'  # instance attribute
        self.location = 'jam er maj khane'

    def purchase(self, item, price, amount):
        remaining = amount-price
        print(f'bying:{item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multiply(a, b):
        print(a*b)

    @classmethod
    def hudai_dekhi(self, item):
        print('hudai dekhi kinto kinbo na AC e hawa khaite aisi', item)


# Shopping.purchase('a', 2, 3, 4)
basundhara = Shopping('basun dhara', 'not popular location')
# basundhara.purchase('lungi',500,1000)
basundhara.hudai_dekhi('bal')
Shopping.hudai_dekhi('dim')

Shopping.multiply(4, 5)
basundhara.multiply(7,9)