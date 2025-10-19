from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run ")
class dog(animal):
    def move(self):
        print("i can bark ")
class snake(animal):
    def move(self):
        print("i can hiss ")
class cat(animal):
    def move(self):
        print("i can meow ")
h1=human()
h1.move()
c1=cat()
c1.move()
s1=snake()
s1.move()