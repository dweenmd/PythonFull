class phone:
    manufactured = 'china'

    """
    this is void constractor
    def__init__(self,brand,sms):
        pass
        
    """
    # example of constractor

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'sending to :{phone}{sms}'
        print(text)


my_phone = phone('kala chan', 'oppo', '18,000')
print(my_phone.owner, my_phone.brand, my_phone.price)
