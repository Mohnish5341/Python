f=open('sample.txt','r')#f=open('sample.txt')
data=f.read()
print(data)
f.close()

f=open('sample.txt','r')#f=open('sample.txt')
data=f.readline()#Read a first line
print(data)
data=f.readline()#Read a next line
print(data)
data=f.readline()#Read a third line
print(data)
f.close()

f=open('sample.txt','r')#f=open('sample.txt')
data=f.read(1)#Read a 1 chracter
print(data)
f.close()

# r to read
# w to write
# a to append

f=open('sample2.txt','w')
data=f.write('Please write here')
f.close()
#appending now
f=open('sample2.txt','a')
data=f.write('We are writing here')
f.close()
#Automitically opening the file using with statment

with open('sample.txt','r') as f:
    a=f.read()
print(a)

with open('sample1.txt','w') as f:
    a=f.write("Good code")
print(a)

#one example
def game():
    return 600
score=game()
with open("score.txt") as f:
    hiscore=f.read()
if hiscore=='':
    with open("score.txt","w") as f:
        f.write(str(score))
elif int(hiscore)<score:
     with open("score.txt","w") as f:
        f.write(str(score))

#multiplication in file
with open(f"multiplication.txt","w") as f:
    for i in range(1,21):
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")
        f.write('\n')
#replace key word in file 
with open(f"multiplication.txt","r") as f:      
    content=f.read()
content=content.replace('0','o')
with open('multiplication.txt','w') as f:
    f.write(content)

#renaming file
import os
oldname="sample3.txt"
newname="sample4.txt"
with open(oldname,'r') as f:
    content=f.read()
with open(newname,'w') as f:
    f.write(content)
os.remove(oldname)
