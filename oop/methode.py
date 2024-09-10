class first_class:
    # attributes
    price = 12000
    product = 'mobile'
    brand = 'samsung'
    features=['camera', 'speaker', 'net browsing facilities']

    # methode with no perameter
    def call(self):  # this is a void function no return value
        print('Calling to others phone')
    
    #methode with perameter and return value
    def send_sms(self,phone ,sms):
        text=f'sending sms to: {phone} and the message is, {sms}'
        return text
        
my_phone= first_class()

print(my_phone.price)
print(my_phone.brand)
print(my_phone.features)
my_phone.call()
print(my_phone.send_sms('01518485428','i love you so much'))