#indexing
a='mohnish'
print(a[0]) #print(a)
print(a[:4]) # print(a[-3:-7])
print(a[1:4]) #print (a[0:4])
print(a[1:4:2]) #skipp one value after each one value
print(a[:-1]) # print(a[0:-1])
print(a[-5:-1]) # print(a[3:7])
print(a[-5:-1:2]) # skipp one value after each one value, not applicable with -values
a='Mohnish is a good boy'
#count
print(a.count('o'))
#capitalize
print(a.capitalize())
#find
print(a.find('good'))
#endswith
print(a.endswith('boy'))
#replace
print(a.replace('good','bad'))#replace all word that match
print(a.count('Harry \n is \t good\\bad boy'))
print(a.count('o'+a+'concatination'))
a='Ram  is  good  boy'
print(a.replace(' ',''))







