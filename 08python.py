def factorial(n):#n!=1*2*3*4*.....*n
    a=1
    for i in range(n):
        a=a*(i+1)
    return a
f=factorial(5)
print(f)

