#first question 
numbers=[10,20,30,40,50]
element=30

#using 'in' operators
if element in numbers:
    print("element present in the list")
else:
    print("element was not present in the list")

#using 'not in' operators
element2=60
if element2 not in numbers:
    print("element2 was not present in list")
else:
    print("element2 was present in list")

#second question
a=[10,20,30,40,50,60,70,]

print(a[0])

print(a[-1])

print(a[1:])

#third question 
a=[1,2,3,4,5,6,7]

a.append(8)
print(a)

a.insert(4,6)
print(a)

#using pop method
a.remove(2)
print(a)

#using remove method
a.remove(4)
print(a)

#fourth question
a=[1,2,3]
b=[4,5,6]

#concatanationn
c=a+b
print(c)

#repetation
print(a*4)

#length
print(len(a))

#max value
print(max(a))

#min value
print(min(a))
