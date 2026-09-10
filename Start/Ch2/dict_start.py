# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydict = {
  "key1" : 1,
  "key2" : 2,
  "key3" : 3,
  "key4" : 4,
  3 : "three",
  4.5 : ["four point five"]
}

# dictionaries are accessed via keys
mydict["seven"] = 7

# you can also set dictionary data by creating a new key


# Trying to access a nonexistent key will produce an error


# To avoid this, you can use the "in" operator to see if a key exists
# print("two" in mydict) # False
# print("key1" in mydict) # True

# # You can retrieve all of the keys and values from a dictionary
# print(mydict.keys())
# print(mydict.values())

# You can also iterate over all the items in a dictionary
for key, val in mydict.items():
  print(f"key: {key}, value: {val}")