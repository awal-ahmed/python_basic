
# Allignment is most important
x= input("x: ")
y= input("y: ")


# if
if(x>y):
    print("x is greater than y")





# else
if(x>y):
    print("x is greater than y")
else:
    print("x is not greater than y")




#elif
if(x>y):
    print("x is greater y")
elif(x<y):
    print("y is greater x")
else:
    print("both number is equal")





z=input("z :")

if(x>y and x>z):
    print("x is the biggest")
elif(y>x and y>z):
    print("y is the biggest")
elif(z>x and z>y):
    print("z is the biggest")
else:
    print("at least two of them are equal")



#nested if
if(x>y and z>y):
    if(z>y):
        print("z is the biggest")
    elif(x>z):
        print("x is the biggest")
else:
    print("x and z are equal")
