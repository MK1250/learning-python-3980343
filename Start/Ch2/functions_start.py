# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# hello_func()

# function that takes parameters
# def hello_func(greeting, name):
#   print("Hello World!")
#   print(greeting, name)

# hello_func("Nice to meet you,", "Alice")


# function that returns a value
# def cube(x):
#   return int(x) * int(x) * int(x)

# num = input("Enter a number to cube: ")
# print(cube(num))

# function with default value for an parameter
# def hello_func(greeting, name=None):
#   print("Hello World!")
#   if name == None:
#     name = input("What is your name? ")
#   print(greeting, name)

# hello_func("Nice to meet you,")

# function with variable number of parameters
def multi_add(start, *args): # we use args when we don't know how many parameters will be passed to the function
  total = start
  for a in args:
    total = total + a
  return total

print(multi_add(10, 1, 2, 3, 4, 5))
