
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

# Times and dates can be formatted using a set of predefined string
# control codes 
now = datetime.now() # get the current date and time

#### Date Formatting ####

# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%a, %d, %B, %y"))

# %c - locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("the current locale date and time is: %x %X"))

#### Time Formatting ####

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("Current time: %I: %M:%S %p"))
print(now.strftime("Current time: %I: %H:%M"))
