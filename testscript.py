class Mammal:
    def __init__(self, name, age):
        self.name = name
        self.steps_taken = 0
        self.age = age

    def walk(self):
        self.steps_taken += 1
        return self.steps_taken


class Dog(Mammal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print("Voff!!")

    @staticmethod
    def hello():
        print("sniffing you ass")


bob = Dog("bob", 2)

charlie = Dog

for x in range(10):
    for y in range(10):
        bob.walk()
    bob.bark()
print(bob.steps_taken)
bob.bark()

print("test")
Dog.hello()

grades = map(int, '90, 40, 10'.split(', '))
print(list(grades))
