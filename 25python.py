try:
    with open('1.python.py',r) as f:
        f.read()
    with open('2.python.py',r) as f:
        f.read()
    with open('122.python.py',r) as f:
        f.read()
except Exception as e:
    print('Any of the above file is not present')     

l=[1,2,3,4,5,6,7,8]
for index,item in enumerate(l):
    if (index+1==1 or index+1==3 or index+1==7):
        print(item)

num= int(input('Enter a number:'))
multiplication = [i*num for i in range(1,11)]
print(multiplication)

with open('mul.txt','w') as f:
    f.write(str(multiplication))
