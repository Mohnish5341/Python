#Multiple Inheritance
class Employee:
    company='Fiverr'
    eCode=120
class Freelancer:
    company='Visa'
    level=0
    def upgradelevel(self):
        self.level=self.level+1
        print(self.level)
class Programmer(Freelancer,Employee):
    name='Rohit'

p=Programmer()#All properties of two parent class inherated here
p.upgradelevel() 
print(p.company)#it will give 1st priority to Freelancer class as in the parameter it is written 1st