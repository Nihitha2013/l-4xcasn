from abc import ABC, abstractmethod
class aclass(ABC):
    def print(self,x):
        print("Value which is passed is:", x)

    @abstractmethod
    def task(self):
        print("Inside Abstract")

class testclass(aclass):
    def task(self):
        print("Inside test class")

obj=testclass()
obj.task()
obj.print(50)