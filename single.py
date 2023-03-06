class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")

class Dog(Animal):
    def bark(self):
        print("The dog barks")

d = Dog()
d.fur()
d.legs()
d.bark()
