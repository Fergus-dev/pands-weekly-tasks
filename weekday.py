# weekly task for week 05
# writing a program to tell me whether or not today is a weekday

import datetime
from datetime import date

yyyy_mm_dd = datetime.date.today()

today = datetime.date.weekday(yyyy_mm_dd)

if today >= 0 and today < 5:
    print("Unfortunately, today is a weekday :( .)")
elif today > 5:
    print("Finally the weekend")

