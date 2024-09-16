# lambda function
print('Hello world')
def  divide2(n,y):
    return n/y
# Instead of this we can use lambda function
print(divide2(4,2))
divide1 = lambda x,y: x/y
print(divide1(10,2))

# join functon
friends =['Rohit','Shubham','Tripti','Neha']
a = ' is a friend of '. join(friends)
b = ' and '. join(friends)
print(a)
print(b)

#format function
a = 'I am a good boy a on {1} and a friend of {0}'.format('Earth', 'Harry')
print(a)
b = 'I am a good boy a on {} and a friend of {}'
a = b.format('Earth', 'Harry')
print(a)

#Map, Filter & Reduce

square1 = lambda x: x*x
l = [1,2,3,4,5]
c = map(square1,l)
print(list(c))

greater1 = lambda x: x>5
a = [1,2,23,3,4,5,6,7,8,9,4,1,32,4]
b = filter(greater1,a)
print(list(b))

from functools import reduce
sum1 = lambda x, y: x+y
i = [1,2,3,7]
j = reduce(sum1, i)
print(j)

def max1(m,n):
    if m>n:
        return m
    return n
a=[1,33,435435,45]
maxNum = reduce(max1,a)
print(maxNum)

a = [i*2 for i in range(1,11)]
st = ''
for item in a:
    st += str(item)+'\n'
print(st)

