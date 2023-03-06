class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")

class Name:
    def me(self):
        print("I am a dog")

class Dog:
    def bark(self):
        print("The dog barks")

class Habitat(Animal, Name, Dog):
    def home(self):
        print("I live in people's homes")
    def dom(self):
        print("I am a domestic animal")

h = Habitat()
h.fur()
h.legs()
h.me()
h.bark()
h.dom()
h.home()
