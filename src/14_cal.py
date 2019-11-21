"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

calendar.setfirstweekday(calendar.SUNDAY)

x = input("Enter year, month (ex. 2019,11): ").split(",")


def user_input(*date_input):
    # no input
    if x[0] == '':
        print('No date values were input.  The current year and month is: ')
        return calendar.month(datetime.now().year, datetime.now().month)

    # if only month was input
    elif len(date_input) == 1:
        return calendar.month(datetime.now().year, int(date_input[0]))

    # if both year and month were input
    elif len(date_input) == 2:
        input_year = int(date_input[0])
        input_month = int(date_input[1])

        if isinstance(input_year, int) and 0 < input_month <= 12:
            return calendar.month(input_year, input_month)
        else:
            return calendar.month(datetime.now().year, datetime.now().month)

    # incorrect number of arguments passed
    print("too many arguments passed")


print(user_input(*x))
