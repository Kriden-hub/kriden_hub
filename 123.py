class Animal:
    def __init__(self, name, number, ration):
        self.name = name
        self.number = number
        __week = 7
        self.ration = ration*__week

    def make_sound(self): #полиморфизм
        pass

    def __str__(self):
        return f"Животное имя: {self.name},{self.number}"

  #  def __count_food(self):
 #       return self.ration*7

    def show_week_ration(self):
        print(self.__count_food())



class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} meow")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} wow")

cat = Cat("Bob", 12, 100)
print(cat)
cat.make_sound()
print (cat.ration)
