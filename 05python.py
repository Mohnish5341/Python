
#Dictionary
myDist={
    "Fast":"In a Quick Manner",#unorder in nature and muitable
    "Harry":"A Coder",
    "Marks":[1,2,5],
    "anotherdict":{'harry':'Player'}
}
print(myDist['Fast'])
print(myDist['Harry'])
print(myDist['Marks'])
print(myDist['anotherdict']['harry'])
myDist['Fast']='Mohnish'
print(myDist['Fast'])
print(list(myDist.keys()))#list of keys
print(list(myDist.values()))#list of values
print(list(myDist.items()))#list of items
#adding in dictionary
updateDist={"name":"Mohnish"}
myDist.update(updateDist)
print(myDist)
#Calling using key
print(myDist.get('Harry1')) #if key in not exist then will not show error return none
print(myDist['Harry'])
#sets
a={1,2,1,3,4,5,9}#Ignore duplicate values
print(a)
a={} #EMpty disctionary
a1=input('Enter the string')
a2=input('Enter the string')
a3=input('Enter the string')
a['Mohnish1']=a1
a['Mohnish2']=a2
a['Mohnish3']=a3
print(a)
b=set()#empty set
b.add(0)#adding in set
print(a)
b.remove(0)#removing in set
print(b)
print(len(a))#length
#We can't add list and dictionary but can tupples as it is immutiable
b={4,8,9,77,4}
print(b.pop())#remove arbitary no.from the set
print(b.clear())#remove all no.from the set
c={6,98,6,8}
print(b.union(c))#union of b and c
print(b.intersection(c))#common of b and c



