#Property Decorator
class Employee:
    company='Camel'
    salary=100
    location='Delhi'

    @property
    def length(self):
        return self.a
    @length.setter
    def length(self, value):
        self.a=value
emp=Employee()
emp.length = 78
#Instead of using this you can user @property print(emp.length())
print(emp.length)

