class Animal :
    def __init__(self) :
        print("An animal is created.")

class Dog(Animal) :
    def __init__(self) :
        super().__init__()  # Call the constructor of the base class
        print("A dog is created.")

d1 = Dog()        