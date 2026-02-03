class Animal :
    def speak(self) :
        print("the animal speaks.")

class Dog(Animal) :
    def speak(self):
        print("The dog barks.")

d1 = Dog()
d1.speak()  # The dog barks.

d2 = Animal()
d2.speak()  # the animal speaks.