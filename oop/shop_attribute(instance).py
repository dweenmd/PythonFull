class Shop:
    shopping_mall='jamuna'
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[] #cart is an instace attribute

    def add_to_cart(self,item):
        self.cart.append(item)
KomolaBanu=Shop('Komola Banu')
KomolaBanu.add_to_cart('shoe')
KomolaBanu.add_to_cart('phone')
print(KomolaBanu.cart)

lalumia=Shop('Lalu Mia')
lalumia.add_to_cart('shirt')
lalumia.add_to_cart('pant')

print(lalumia.cart)