i=1
while (i<=90):
    print(i)
    i = i + 1
for a in range(1,10):
    print(a)
k=[1,2,3,4,4,5,6,6]
for i in k:
    print(i)
else:
    print("Loop is completed")

for i in k:
    print(i)
    if(i==3):
        break
else:
    print("Loop is completed")

for i in k:
    print(i)
    if(i==3):
        continue
else:
    print("Loop is completed")

a=int(input("Enter the no "))
for i in range(1,11):
    print(f"{a}X{i}={a*i}")

a=['sadf','sdfsdf','sdfsd']
for i in a:
    if i.startswith('s'):
        print("Start with S"+i) 
a=int(input("Inter the no"))
prime=True
for i in range(2,a):
    if(a%i==0):
        prime=False
        break
if prime:
    print("This no. is Prime")
else:
    print("This is not prime")

n=4
for i in range(4):
    print(' '*(n-i-1),end='')
    print('*'*(2*i+1),end='')
    print(' '*(n-i-1))