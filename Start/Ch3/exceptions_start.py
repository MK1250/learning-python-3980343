# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
# x = 10 /0
# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
# 0


# You can also catch specific exceptions
# try:
#   answer = input("Provide a number to divide 10 by: ")
#   num = int(answer)
#   print(10/num)
# except ZeroDivisionError as e:
#   print("You can't divide by zero!")
# except ValueError as e:
#   print("You must provide a valid number!")
#   print(e)
# finally:
#   print("This code always runs, regardless of whether an exception was thrown or not.")



  # Code Challenge: Palindromes
  # Python code​​​​​‌​​​​​​‌‌‌‌​​‌​​​​​‌​‌‌‌‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False
import string

def is_palindrome(teststr):
    # turn all characters to lower case
    temp = teststr.lower()

    # remove all punctuation and spaces from the string
    newstr = ""
    for c in temp:
      if c.isalnum():
        newstr = newstr + c

    # new calculate the reverse of the string
    revstr = ""
    strindx = len(newstr) - 1
    while strindx >= 0:
       revstr = revstr + newstr[strindx]
       strindx = strindx - 1

    if newstr == revstr:
        return True
    else:
        return False


# This is how your code will be called.
# Your answer should determine whether a string is a palindrome.
# You can edit this code to try different testing cases.

test_word = "Madam, I'm Adam."
result = is_palindrome(test_word)
print(f"Is the string '{test_word}' a palindrome? {result}")

# try using some of these other words:
test_word = "RACE CAR!"
result = is_palindrome(test_word)
print(f"Is the string '{test_word}' a palindrome? {result}")

test_word = "Hello, world"
result = is_palindrome(test_word)
print(f"Is the string '{test_word}' a palindrome? {result}")

test_word = "Radar?"
result = is_palindrome(test_word)
print(f"Is the string '{test_word}' a palindrome? {result}")

test_word = "A man, a plan, a canal Panama!"
result = is_palindrome(test_word)
print(f"Is the string '{test_word}' a palindrome? {result}")
