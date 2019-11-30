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


def cal():
    message = input()
    split = message.split(' ')
    _cal = calendar.TextCalendar(6)  # 6 is starting the week at Sunday
    if message == '':
        today = datetime.today()
        _cal.prmonth(today.year, today.month)
    elif len(split) == 1 and 12 > int(split[0]) > 0:
        today = datetime.today()
        _cal.prmonth(today.year, int(split[0]))
    elif len(split) == 2 and 12 > int(split[1]) > 0:
        _cal.prmonth(int(split[0]), int(split[1]))
    else:
        print('''
# Usage: Enter nothing to get the current month.
# Enter a single month from 1-12 to get that month in the current year.
# Enter a year and a month as integers separated by a space to get that month and year.
            ''')


cal()
