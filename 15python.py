#Supper 
class Person:
    def __init__(self):
        print("I am a parent of parent constractor")
    def takeBreath(self):
        print("I am breathing")
class Employee(Person):
    def __init__(self):
        super().__init__()
        print("I am a parent constractor")
    def takeBreath(self):
        super().takeBreath()#go to parent 1st
        print("I am an Employee so i am luckily breathing")
class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("I am a constractor")
    def takeBreath(self):
        super().takeBreath()#go to parent 1st
        print("I am an Programmer so i am luckily breathing ++")
# if any of the method or variable is not present in child table then it will inherate from his parent class and if it is not ther than parent of parent class data in inherated
pr=Programmer()
pr.takeBreath()
pr.__init__()





