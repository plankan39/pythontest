class Mammal:
    def __init__(self, name):
        self.name = name
        self.steps_taken = 0

    def walk(self):
        self.steps_taken += 1
        return self.steps_taken


class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print("Voff!!")


bob = Dog("bob")

for x in range(10):
    for y in range(10):
        bob.walk()
    bob.bark()
print(bob.steps_taken)


