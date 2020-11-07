# sometime
Get timestamp, formatted date, and perform date/time operations.

```python
from sometime.sometime import Sometime

date = Sometime()
print(date.timestamp())

# access dictionary
moment = date.moment()

# to add/subtract, set parameter to any positive/negative integer
date.year(1) # month(), day(), hour(), minute(), second()
print(date.year())

# custom date increments / decrements
# date.add(years=0, months=0, days=0, hours=0, minutes=0, seconds=0)
date.add(years=5, months=1, days=7)
date.add(hours=1, minutes=30)
date.add(minutes=1, seconds=25)

# Name of Month e.g. November
print(date.name_of_month()) 

# Day of Week e.g. Monday
print(date.day_of_week()) 

# AM / PM
print(date.period())

# Custom date formats
print(date.("%Y-%m-%d %H:%M:$S"))

```
