# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
print("text to display")
print(mystr)


# Operators are used to perform operations on variables
# print(myint + myfloat)
# print(myint * myfloat)
# print(myint / myfloat)
# print(myint % 3)

another_str = "This is another string"
print(mystr + another_str)
print("num " * 3)


# Logical and comparison operators 
print(myint > 5)
print(myfloat == 13.2576)
print(mystr != another_str)
print(mybool and False)
# re-declaring a variable works
myint = "abc"
print(myint)
