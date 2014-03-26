datecalc
========
######v2.0.2

datecalc is created by Violet (http://pariahvi.com) and is licensed under a BSD License. Read LICENSE.txt for more license text.

Python module to calculate the day of the week of any date

####Dependencies
* Python (>= 2.4)

To install, open the terminal and `cd to the root directory of this program, then enter the command:
```
sudo python setup.py install
```

You could also install this module using pip (Recommended Method) by entering the command:
```
sudo pip install datecalc
```

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
