
height = 170
sexuality = 0




class Charater:
    def __init__(self, name):
        self.name = name
        self.height = height
        self.age = 18

    def sayHello(self):
        print(f"Hi my name is {self.name} and Im {self.age} years old!")
    
    

Teemo = Charater("Teemo")

Teemo.sayHello()