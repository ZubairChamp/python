from abc import ABC, abstractmethod
class abcClass(ABC):
    def print(self,x):
        print("passed value is ",x)
    def task(self):
        print("we are inside abc class task ")
class testclass(abcClass):
    def task(self):
        print("we are inside test class task ")
abcobject=abcClass()
abcobject.task()
testobject=testclass()
testobject.task()
testobject.print(100)