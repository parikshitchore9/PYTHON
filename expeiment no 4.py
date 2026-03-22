#first question
#while loop
b=2
while b<=10:
    print(b)
    b+=2

#second question
#while loop
sum=0
num=1
while num < 10:
    sum = sum + num
    num += 2
print(sum)

#third question
#fibonacci series
a=0
b=1

while a<=50:
    print(a)
    c=a+b
    a=b
    b=c

    #fourth question
string = input("enter the string: ")

i = 0
result = ""

# Use 'while' instead of 'when'
# Use '<' instead of '<=' to avoid index errors
while i < len(string):
    if i % 2 == 0:
        result += string[i]
    
    # Increment i OUTSIDE the if-statement so the loop progresses
    i += 1

print("string after removing odd index character:", result)