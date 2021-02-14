###########################################################################################
###########################################################################################
# Find the last day of the month

# This example and information was found in the article posted here:
# https://levelup.gitconnected.com/python-tricks-i-can-not-live-without-87ae6aff3af8

# calendar.monthrange(year, month)
# Returns the weekday (0-6 ~ Mon-Sun) of the first day of the month
# & # of days (28-31) for the year, month given

###########################################################################################

import calendar
# let's play with February
calendar.monthrange(2021, 2)
# (0, 28) First day is on Monday & there are 28 days
calendar.monthrange(2022, 2)
# (1, 28) First day is on Tuesday & there are 28 days
calendar.monthrange(2023, 2)
# (2, 28) First day is on Wednesday & there are 28 days
calendar.monthrange(2024, 2)
# (3, 29) First day is on Thursday & there are 29 days for Leap Year!!
calendar.monthrange(2025, 2)
# (5, 28) First day is on Saturday & there are 28 days

###########################################################################################
###########################################################################################

# Find the weekday for any day

# This example and information was found in the article posted here:
# https://levelup.gitconnected.com/python-tricks-i-can-not-live-without-87ae6aff3af8

###########################################################################################

from datetime import datetime
mydate = datetime(2024, 2, 15)
datetime.weekday(mydate)
# will result:
3
# or:
datetime.strftime(mydate, "%A")
'Thursday'

###########################################################################################
###########################################################################################

# Determining leap years

# This example and information was found in the article posted here:
# https://levelup.gitconnected.com/python-tricks-i-can-not-live-without-87ae6aff3af8

###########################################################################################

# checking if year is leap:
calendar.isleap(2021)  # False
calendar.isleap(2024)  # True
# or checking how many days will be leap days for given year span:
calendar.leapdays(2021, 2026)  # 1
calendar.leapdays(2020, 2026)  # 2
# read the help here, as range is: [y1, y2), meaning that second
# year is not included;
calendar.leapdays(2020, 2024)  # 1

###########################################################################################
###########################################################################################

