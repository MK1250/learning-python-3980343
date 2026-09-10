# LinkedIn Learning Python course by Joe Marini
# Example file for using built-in functions
#

# mystring = "The quick, brown fox jumped over the lazy dog!"
# mynumbers = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence
# print(len(mystring))
# print(len(mynumbers))

# # the max() and min() functions will find the largest and smallest value in a sequence
# print(max(mynumbers))
# print(min(mynumbers))

# the str() function will return a string version of an object
# prefix = "result: "
# result = 5
# print(prefix + str(result))


# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 
# print(list(range(5, 10)))

# for i in range(5, len(mystring), 2):
#   print(mystring[i])

# # the print function itself is pretty flexible - you can embed variables directly in it
# greeting = "Hello!"
# count = 10
# print(f"{greeting} you are visitor number {count} to this site today.")


# Code Challange: Find the Longest string
show_expected_result = False
show_hints = False

def find_largest(numbers):
    largest = "starter string"
    for s in numbers:
        if len(s) > len(largest):
            largest = s
    return len(largest)

test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]
result = find_largest(test_strings)
print(f"the length of the largest string is: {result}")