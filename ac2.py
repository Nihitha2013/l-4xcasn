from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("Human can walk")
class lion(animal):
    def move(self):
        print("Lion can roar and can walk")
class fish(animal):
    def move(self):
        print("Fish can swim")
nihitha=human()
nihitha.move()
cub=lion()
cub.move()
bluee=fish()
bluee.move()
