class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


person1 = Person("john", 5)
person2 = Person("john", 5)

print("Override")
print(person1 == person2)
print(person1 is person2)


class Animal:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


animal1 = Animal("john", 5)
animal2 = Animal("john", 5)

print("No Override")
print(animal1 == animal2)
print(animal1 is animal2)

print("Different class")
print(person1 == animal1)
print(animal1 == person1)
