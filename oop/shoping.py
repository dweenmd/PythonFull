class shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[]

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def print_cart(self):
        for item in self.cart:
            print(f'Item: {item["item"]}, Price: {item["price"]}, Quantity: {item["quantity"]}')
            
    def checkout(self,amount):
        total=0
        for item in self.cart:
            total+=item['price']*item['quantity']
        print('total price: ', total)
        if amount<total:
            print(f'Please provide {total-amount} more taka.')
        else:
            print(f'here is your items. \nTake Extra money: {amount-total}')

swapan=shopping('alan swapon')
swapan.add_to_cart('alu',50,6)
swapan.add_to_cart('dim',12,24)
swapan.add_to_cart('peyaj',110,5)
swapan.add_to_cart('rice',60,10)
#print(swapan.cart)
swapan.print_cart()
swapan.checkout(10600)
