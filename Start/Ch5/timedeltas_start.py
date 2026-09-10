#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("today is: ", now)

# print today's date one year from now
print("one year from now it will be: ", now + timedelta(days=365))

# create a timedelta that uses more than one argument
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("one week ago it was: ", s)

# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?
today = date.today()
today = date(today.year, 11, 10)
afd = date(today.year, 4, 1)

if afd < today:
  print(f"April Fools' Day already went by {(today-afd).days} days ago")
  afd = afd.replace(year=today.year + 1)

time_to_afd = afd - today
print(f"it's just {time_to_afd.days} days until April Fools' Day!")