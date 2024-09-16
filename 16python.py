#class method(type of static method)
class Employee:
    company='Camel'
    salary=100
    location='Delhi'
    
    # def changeSalary(self,sal):
    #     self.__class__.salary=sal

    @classmethod#changing class variable value
    def changeSalary(cls,sal):
        cls.salary=sal
e=Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
