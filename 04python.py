#List muitable
a=[55,7,33]
print(a)
a.sort()#arrange in accending order
print(a)
a.reverse()#arrange in decending order
print(a)
a.append(555)#adding
print(a)
a.remove(555)#removing
print(a)
a.insert(3,555)#At index 3 adding 555
print(a)
a.pop(3)#removing index 3
print(a)
#Tupple immuitable
t=()#Empty tupple
t=(1,2,3)
print(t[0])
t=(1,)#Single element in tupple
print(t)
t=(3,6,7,8,6,9)
print(t.index(6))
print(t.count(6))