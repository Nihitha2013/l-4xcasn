class cat:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("I am cat. My name is ", self.name)
        print("Meow Meow")

class dog:
        def __init__(self,name):
            self.name=name
        def make_sound(self):
            print("I am dog. My name is ", self.name)
            print("bark")

cat1=cat("Kitty")
dog1=dog("doggy")

for animal in(cat1,dog1):
     animal.make_sound()