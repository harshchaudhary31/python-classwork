class Animal:
    def __init__(self,age,name):
        self.name=name
        self.age = age
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    
    def __str__(self):
        return f"name is {self.name}\nage is {self.age}"
class dog(Animal):
    species = "Canis familiaris"

    def bark(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    species ="Cat species"

    def meu(self):
        return f"{self.name} says meu!"

dog1 = dog("Buddy",3)
cat1 = Cat("Charlie",5)

print(dog1)
print(cat1)
