#read only --> you can not set the value.value can not be changed
#getter --> get a value of a property through a methode .Most of the time , you will get the value of a private attribute
#setter--> set a value of a property through a method. most of the time you will set the value of a private property
 
class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    # Getter without any setter is a read-only attribute
    @property
    def age(self):
        return self._age
    
    # Getter
    @property
    def salary(self):
        return self.__money

    # Setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            print('Salary cannot be negative')
        else:
            self.__money += value

samsu = User('kopa', 21, 12000)

print(samsu.age)
print(samsu.salary)
samsu.salary=4500
print(samsu.salary)
