#constructor
class Employee1:
    company='google'#class variable
    def __init__(self,name,salary,submit):# working as a constructor
        self.name= name
        self.salary=salary
        self.submit=submit
        print('Employee is created')
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.submit}")
    def getsalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
        print(signature)
    @staticmethod
    def greet():
        print('Good Morning, Sir')
    @staticmethod
    def time(T1):
        print(f'time is {T1}')

#ob1 = Employee1()--> This throws an error *(missing 3 required positional)
ob1 = Employee1('Mohnish',100,'youtube')
ob1.getDetails()

#calculator
class calculator:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def square(self):
        print(self.number1*self.number1)
    def substract(self):
        print(self.number1-self.number2)
    def add(self):
        print(self.number1+self.number2)
    def percentage(self):
        print(self.number1/100)
ob=calculator(10,2)
ob.square()
ob.substract()
ob.add()
ob.percentage()

#calling class attribute and instance attribute
class num:
    a=999
ob=num()
ob.a=111
print(f"instance attribute {ob.a} class attribute {num.a}")


# train ticketing tool
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getseats(self):
        print('**************')
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train is {self.seats}")
        print('**************')
    def getfare(self):
        print(f"The price of the ticket is {self.fare}")
    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your ticket number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("No Ticket is available! Please try tatkal")
    def cancelticket(self):
        if(self.seats<2):
            print(f"Seat is cancled")
            self.seats=self.seats+1
            print(f'current seat available {self.seats}')
        else:
            print('No seats booked')


ob=Train("ND234",1400,2)
ob.getseats()
ob.getfare()
ob.bookticket()
ob.bookticket()
ob.cancelticket()