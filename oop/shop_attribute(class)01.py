class shop:
    cart=[]  #this cart is a class attribute(shares with all instace)
    def __init__(self,buyer):
        self.buyer=buyer

    def add_to_cart(self,items):
        self.cart.append(items)

KomolaBanu=shop('Komola Banu')
KomolaBanu.add_to_cart('shoe')
KomolaBanu.add_to_cart('phone')
print(KomolaBanu.cart)

lalumia=shop('Lalu Mia')
lalumia.add_to_cart('shirt')
lalumia.add_to_cart('pant')

print(lalumia.cart) # this class attribute add all items in cart(error!!)