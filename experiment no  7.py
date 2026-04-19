#question no 1
a=(1,2,3)
b=(4,5,6)

#length 
print(len(a))
print(len(b))

#concatenation
print(a+b)

#repetation
print(a*5)
print(b*5)

#membership
print(3 in a)
 
#question no 2
#indexing
print(a[1])

#negative indexing
print(b[-2])

#slicing
print(a[1:])

#iteration
for x in a:
    print(b)

#question no 3
#tuples are immutable
print(a.append(4)) #shows that tuples are immutable

#deleting the tuple
del a
print(a)

#question no 4
m=(11,22,33,44)
n=(55,66,77,88)
#len()

print(len(m))

#max()
print(max(n))

#min()
print(min(m))

#tuple
print(tuple(m))