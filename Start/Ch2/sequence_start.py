# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = ["no", "freaking", "way"]
myTuple = ("tuple", "freaking", "way")

# to access a member of a sequence type, use []
# print(mylist[-1])
# print(myTuple[0])

# add a list to another list
# another_list = ["no", "freaking", "way"]
# mylist = mylist + another_list
# print(mylist)
# mylist.append("no")
# print(mylist)


# use slices to get parts of a sequence
# print(mylist[::-1])

# you can use slices to reverse a sequence


# Tuples are like lists, but they are immutable
mytuple = ("tuple", "freaking", "way")
# tuples cannot be changed, so the following will cause an error
# mytuple[0] = "no"


# Sets are also sequences, but they contain unique values
myset = {"no", "freaking", "way"}
# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership: checking if a value is in a sequence
print("no" in myset)
print("freaking" in myset)