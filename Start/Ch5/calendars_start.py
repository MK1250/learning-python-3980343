#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# thestr = c.formatmonth(2026, 1, 0, 0)
# print(thestr)

# create an HTML formatted calendar
# HC = calendar.HTMLCalendar(calendar.SUNDAY)
# thestr = HC.formatmonth(2026, 1)
# print(thestr)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2026,9):
#   print(i)
  
# # The Calendar module provides useful utilities for the given locale,
# # such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#   print(name)

# for day in calendar.day_name:
#   print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
# print("Team meetings will be on:")
# for m in range(1,13):
#   cal = calendar.monthcalendar(2026, m)
#   weekone = cal[0]
#   weektwo = cal[1]

#   if weekone[calendar.FRIDAY] != 0:
#     meetday = weekone[calendar.FRIDAY]
#   else:
#     meetday = weektwo[calendar.FRIDAY]
#   print(f"{calendar.month_name[m]} {meetday }")



  # Code Challenge: Dates and times
  ## Count the number of instances of a particular weekday in a given month/year.

 # Return the number of instances of a particular weekday in a given month/year.
show_expected_result = False
show_hints = False

def count_days(year, month, whichday):
  count = 0
  cal = calendar.monthcalendar(year, month)
  for week in cal:
    if week[whichday] != 0:
        count +=1
  return count

testyear = 2025
testmonth = 12
testday = 0
result = count_days(testyear, testmonth, testday)
