class calculator:
    brand = 'casio MS-100'
    def add(self,num1,num2):
        print(f'summation of {num1} and {num2} : {num1+num2}')
    def deduct(self,num1,num2):
        print(f'deduct of {num1} and {num2} : {num1-num2}')
    def mul(self,num1,num2):
        print(f'multiplication of {num1} and {num2} : {num1*num2}')
    def div(self,num1,num2):
        print(f'divition of {num1} and {num2} : {num1/num2}')
    
cal=calculator()
cal.add(4,5)
cal.deduct(8,3)
cal.mul(4,8)
cal.div(15,2)
