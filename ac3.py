class USA():
    def capital(self):
        print("Washington, D.C ic capital of USA")

    def type(self):
        print("USA is a developed country")

class Japan():
    def capital(self):
        print("Tokyo is capital of Japan")

    def type(self):
        print("Japan is a highly developed country")

objUSA=USA()
objJap=Japan()

for c in (objJap,objUSA):
    c.capital()
    c.type()

