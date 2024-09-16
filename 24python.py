#global
#enumerate
a= 9
def func():
    global a
    a = 8
    print(a)
    a = 900
    print(a)
print(a)
func()
print(a)

a=[1,2,3,4,'apple']
# i=0
# for item in a:
#     i=i+1
#     print(f"Iteam number {i} is {item}")

for i, item in enumerate(a):
    print(f"Iteam number {i+1} is {item}")

#list comprehensions
l1=[1,2,3,4,5,6]
#l2=[]
# for item in l1:
#     l2.append(item*item)
l2=[i*i for i in l1 if 1>2]
print(l2)


