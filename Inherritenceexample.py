class Animal :
    def speak(self) :
        print("The animal speaks.")

class Dog(Animal) :
    def bark(self):
        print("The dog barks.")

d1 = Dog()
d1.bark() # The dog barks.
d1.speak() # The animal speaks.
