# class Complex:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,obj):
#         return Complex(self.a + obj.a, self.b + obj.b)
    
# c1=Complex(1,4)
# c2=Complex(11,3)
# c3=c1*c2
# print(c3.a, c3.b)



# class Vector:
#     def __init__(self,l1) -> None:
#         self.dim=len(l1)
#         self.data=l1
#     def __add__(self,obj):
#         mylist = []
#         for i in range(len(obj.data)):
#             mylist.append(obj.data[i] + self.data[i])
#         return Vector(mylist)
#     def __mul__(self,obj):
#         dot = []
#         for i in range(len(obj.data)):
#             dot.append(obj.data[i] + self.data[i])
#         return dot
#     def __len__(self):
#         return len(self.data)


#     v1 = Vector([1, 2, 3])
#     v2 = Vector([11, 12, 13])
#     v3 = v1 + v2
#     v4 = v1 * v2
#     print(v3.data)
#     print(v4)
#     print(len(v3))
