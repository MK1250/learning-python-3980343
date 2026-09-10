# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# answer = input("type exit to exit: ")
# while answer != "exit":
#   print(answer)
#   answer = input("type exit to exit: ")

# define a for loop
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:
  print(d)


# # use a for loop over a collection
# for x in ["a", "b", "c"]:
#   print(f"x is currently: {x}")

# # use the break and continue statements
for d in days:
  if d == "Wed":
    continue
  print(d)

# using the enumerate() function to get an index and an item
for i, d in enumerate(days):
  print(i, d)

# Python code​​​​​‌​​​​​​‌‌‌‌​​​‌‌‌​‌‌‌‌​​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_numbers(which, numbers):
    oddCount = 0
    evenCount = 0
    for d in numbers:
        if d % 2 ==0:
            evenCount = evenCount + 1
        else:
            oddCount = oddCount + 1

    if which == "even":
        return evenCount
    elif which == "odd":
        return oddCount
    return -1