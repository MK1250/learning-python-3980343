#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
print(date.today())

# print out the date's individual components
print("Date components:", date.today().day, date.today().month, date.today().year)

# retrieve today's weekday (0=Monday, 6=Sunday)
print("Today's Weekday # is:", date.today().weekday())
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Which is a:", day[date.today().weekday()])

## DATETIME OBJECTS
# Get today's date from the datetime class
print(datetime.now())

# Get the current time
t = datetime.time(datetime.now())
print(t)
