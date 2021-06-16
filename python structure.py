# Comment

# Single line comment use #
"""triple quotes are used to create multiline string.
If thoser dosen't store in any variable those works as mulitiline comment"""





# Data types

integer = 5                     #int
real = 21.5                     #float
complex_number = 2+5j           #complex
word = "My first program"       #str/ string
boolean = True                  #bool True/Fasle or 1/0



print(type(integer))            #type() function returns the type of the variable
                                #print() function prints the output
#Change the variables to see their type eg. integer, real, complex_number, word, boolean,






#Variables

#variables can be any any name. 
#It must start with alphabet. And can contain alphabet 'A-Z''a-z', number '0-9' and underscore '_'
#Depending on assigned value variables will change type
x= 5
print(type(x)) 
x="A"
print(type(x)) 
X=2.5
print(type(X))                  #case sensitive






#type Conversion/Casting

# from all other to int
float_to_int = int(21.5)
print(float_to_int)
print(type(float_to_int))

str_to_int = int("12")
print(str_to_int)
print(type(str_to_int))

str_to_int = int("A")           #strings other than numaric can't be converted
str_to_int = int("12.5")        #not an integer number

bool_to_int = bool("True")
print(bool_to_int)
print(type(bool_to_int))
# change type with int(), float(), str(), bool(), complex()

#bool function always provides true other these 
x=bool(False)
x=bool(None)
x=bool(0)
x=bool("")
x=bool(())
x=bool([])
x=bool({})








#Operations 

#Arithmetic Operators: +, -, *, /, %(mod), **(Power), //(floor division)
x=5+3
print(x)
#Change the operator to see the effect



#comparison Operators: ==, !=, >, <, >=, <=
x= (5==6)
print(x)
#Always returns bool output


#Logical Operators: and, or, not

#Bitwise Operators: &(and), |(or), ^(X-or), ~(not), <<(left shift), >>(right shift)
#For details "https://www.w3schools.com/python/python_operators.asp"




#input
x=input()
print(x)

y=input("inter your name: ")
print(y)























#any(), some() 

#other type 
"""Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview"""


#List unpack list --> x,y,z=[1,2,3]
