a='harry'#variable can't start with n0. and can't have space 
b="harry"#variable are case sensitive
c='''harry'''
d='''"harry"'''
e='''harry'''
k='"harry"'
f=133
g=False
h=True
i=None
j=2.4
print(a,b,c,d,e,f,g,h,i)
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h),type(i),type(j))#Data types
print(23>3)
#logical operators
bool1=True
bool2=False
print(bool1 and bool2)
print(bool1 or bool2)
print(not bool2)
#type casting
a='333'
a=int(a) 
#input function
print('Enter your no.',int(input()))#it will always take as a string
#average of no.
a=int(input("enter no.1"))
b=int(input("enter no.2"))
print((a+b)/2,(a*a),(b*b))