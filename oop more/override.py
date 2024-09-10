class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polau korma')

    def exercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team

        super().__init__(name, age, height, weight)
    # over ride

    def eat(self):
        print('vegatable')

    def exercise(self):
        print("gym e poisa dia gam jorau")
    def __add__(self,other):
        return self.age + other.age


sakib = Cricketer('sakib', 34, 5.11, 91, 'bd')
mushi=Cricketer('mushi',35,65,78,'Bd')
sakib.eat()
sakib.exercise()

# plus sign overLoad
print('\n\noverloading example: ')
print(45+63)
print('sakib'+'rakib')
print([12, 98]+[5, 6, 7, 1, 2])
