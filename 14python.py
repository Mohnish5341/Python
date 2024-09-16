#Multilevel Inheritancey
class Person:
    country="India"
    def takeBreak(self):
        print("I am breathing")
class Employee(Person):
    company="Honda"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    def takeBreath(self):
        print("I am an Employee so i am luckily breathing")
class Programmer(Employee):
    def getSalary(self):
        print(f"No salary to programmers")
    def takeBreath(self):
        print("I am an Programmer so i am luckily breathing ++")
# if any of the method or variable is not present in child table then it will inherate from his parent class and if it is not ther than parent of parent class data in inherated
p=Person()
p.takeBreak()
e=Employee()
e.takeBreak()
pr=Programmer()
pr.takeBreak()
print(pr.country)
print(pr.company)

