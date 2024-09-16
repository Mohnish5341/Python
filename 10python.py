class Fish:
    def printFish(self):
        print(f"Name of three fishes are:{self.f1}:{self.f2}:{self.f3}")

FISH=Fish()
FISH.f1='fish1'
FISH.f2='fish2'
FISH.f3='fish3'
p=FISH.printFish()

class Sum:
    def SUMS(self):
        return self.a+self.b
s=Sum()
s.a=11
s.b=332
j=s.SUMS()
print(j)

#instance attribute
class Employee:
    company='youtube'#class attribute
    salary=8888#class attribute

Empc=Employee()
Emps=Employee()
Empc.company
Emps.salary
print(f"Before instance/object variable : {Empc.company} {Emps.salary}")
# if want to change salary for a particalar employee
#we use instance variables
Emps.salary=678888
print(f"After instance/object variable : {Empc.company} {Emps.salary}")



class Employee1:
    company='google'#class variable
    def getsalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
        print(signature)
    @staticmethod
    def greet():
        print('Good Morning, Sir')
    @staticmethod
    def time(T1):
        print(f'time is {T1}')
ob=Employee1()
ob.salary=100000#instance variable
ob.getsalary('Thanks!')# Employee1.getsalary(ob)
ob.greet()#Employee1.greet()
ob.time('12:00 pm')#Employee1.time()