class Emp:
    def __init__(self,a,name) -> None:
        self.a=a
        self.name=name
    def __add__(self,obj):
        return self.a + obj.a
    def __str__(self) -> str:
        return self.name
    def __len__(self):
        return self.a

a= Emp(45, "harry")
b= Emp(40, "dfsfs")

print(a,b)
print(len(a))
print(len(b))

