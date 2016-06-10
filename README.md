datecalc
========

datecalc is created by Vi Grey and is licensed under a BSD 2-Clause License. Read LICENSE.txt for more license text.

A Module to Calculate the Day of the Week of Any Date

####Dependencies
* Python (>= 2.4)

####Importing the Module
Simply type:
```
import datecalc
```

####Using the Module
To calculate the day of the week for any date, use *datecalc.date(y, m, d, t)* where y is the full year (a negative integer for BC years), m is the month number, d is the day number, and type is the calendar type.  The calendar types you have to chose from are:
* English
* Roman
* Gregorian
* Julian
* CE

The default type is English, which is the calendar system the English speaking western countries are using.  This is a system where the calendar was under the Julian system until 1752, when it switched to the Gregorian Calendar, skipping  September 3rd and going straight to September 15th to offset for the differences in the calendar systems on how they incorporated leap years.

The Roman calendar system switched to the Gregorian calendar in 1582, going from October 4th streight to October 15th.

####Example Uses
```
import datecalc

print(datecalc.date(2014, 3, 14))
print(datecalc.date(2014, 3, 14, 'English'))
print(datecalc.date(2014, 3, 14, 'Roman'))
print(datecalc.date(-2014, 3, 14))
print(datecalc.date(-2014, 3, 14, 'Julian'))
print(datecalc.date(2014, 3, 14, 'Julian'))
print(datecalc.date(204727298871375019846193105719886136647191237731911139435, 3, 14, 'Julian'))
print(datecalc.date(-204727298871375019846193105719886136647191237731911139435, 3, 14))

```
prints out:
```
Friday
Friday
Friday
Wedneday
Wedneday
Thursday
Monday
Saturday
```
