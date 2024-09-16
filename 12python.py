#Inheritance and mor on opps
class Employee:
    company='Google'
    def showDetails(self):
        print("This is an employee")
class Programmer(Employee):
    language='Python'
    company='Youtube'
    def getLanguage(self):
        print(f"The language is {self.language}")
e=Employee()
e.showDetails()
#e.getLanguage()  >--It will through error
print(e.company)# It will take parent class data only as object is created for parent class
p=Programmer()
p.showDetails()#1st check in child class then in parent class
print(p.company)#overidding as it is present in child class So, It will not take record from parent
p.getLanguage()

