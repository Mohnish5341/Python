class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment
    @property
    def salaryAfterIncrement(self):
        return self.salary * (1+self.increment)
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,a):
        self.salary = a
emp1 = Employee(1000,10)
print(emp1.salaryAfterIncrement)
emp1.salaryAfterIncrement = 12000
print(emp1.salaryAfterIncrement)
