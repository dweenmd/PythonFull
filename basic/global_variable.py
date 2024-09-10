balance = 1000

def buy_things(item,price):
    global balance #declare korte hobe
    print(f'before buying balance is: {balance}')
    balance=balance-price
    print(f'After buying {item} banace is : {balance}')

buy_things('sunglass', 359)