# Copyright (C) 2012-2014, PariahVi
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

# A Module to Calculate the Day of the Week of Any Date

__version__ = '1.0.3.6'
__author__ = 'PariahVi (http://pariahvi.com)'


MONTH_OFFSET = [
    [4, 3], [0, 6], [0], [3], [5], [1], [3], [6], [2], [4], [0], [2]
]
DAYS = [
    'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    'Saturday'
]
CAL_TYPES = [
    'GREGORIAN', 'CE', 'JULIAN', 'ENGLISH', 'ROMAN'
]


# Figure out if leap year for CE style dates.
def ce_leap_year(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return 1
    elif y % 4 == 0:
        return 1
    return 0


# Figure out if leap year for Julian style dates.
def jul_leap_year(y):
    if y < 0:
        y = (y + 1) % 700
    if y % 4 == 0:
        return 1
    return 0


# Figure out if year is a leap year for cal_type.
def is_leap_year(year, cal_type):
    if cal_type == 'GREGORIAN':
        new_year = year
        if year < 0:
            new_year = (year + 1) % 400
        return ce_leap_year(new_year)
    elif cal_type == 'CE':
        return ce_leap_year(year)
    elif cal_type == 'JULIAN':
        return jul_leap_year(year)
    elif cal_type == 'ENGLISH':
        if year >= 1800:
            return ce_leap_year(year)
        else:
            return jul_leap_year(year)
    elif cal_type == 'ROMAN':
        if year >= 1700:
            return ce_leap_year(year)
        else:
            return jul_leap_year(year)


# Check if value is an integer value.
def check_int(value):
    try:
        int(value)
    except ValueError:
        return 0
    return 1


# Check if the date (year, month, date) exists in cal_type.
def is_real_date(year, month, date, cal_type):
    month30 = (4, 6, 9, 11)
    if month not in range(1, 13):
        return 2
    if not check_int(year):
        return 3
    if not check_int(date) or date < 1 or date > 31:
        return 4
    if cal_type not in CAL_TYPES:
        return 5
    if not year and cal_type != 'CE':
        return 6
    else:
        if month in month30 and date > 30:
            return 7
        elif month == 2 and not (date < 29 or (is_leap_year(year, cal_type)
                                 and date == 29)):
            return 7
    if cal_type == 'ENGLISH':
        if month == 9 and date > 2 and date < 14 and year == 1752:
            return 8
    if cal_type == 'ROMAN':
        if month == 10 and date > 4 and date < 15 and year == 1582:
            return 8
    return 1


# Figures out value to add from last two digits of year.
def add_xxyy(year, cal_type):
    new_year = year % 100
    if cal_type != 'CE' and year < 0:
        new_year = (year + 1) % 100
    return ((int(new_year / 12) + (new_year % 12) +
            int((new_year % 12) / 4)) % 7)


# Returns value calculated from every digit of the year besides the last 2
# digits for CE style dates.
def ce_add_yyxx(y):
    yyxx = (2, 0, 5, 3)
    return yyxx[int(y / 100) % 4]


# Returns value calculated from every digit of the year besides the last 2
# digits for Julian style dates.
def jul_add_yyxx(y):
    return (7 - int(y / 100)) % 7


# Figures out value to add from every digit of the year besides the last 2
# digits.
def add_yyxx(year, month, date, cal_type):
    if cal_type == 'GREGORIAN':
        new_year = year
        if year < 0:
            new_year = (year + 1) % 400
        new_year = new_year % 400
        return ce_add_yyxx(new_year)
    elif cal_type == 'CE':
        new_year = year % 400
        return ce_add_yyxx(new_year)
    elif cal_type == 'JULIAN':
        new_year = year
        if year < 0:
            new_year = (year + 1) % 700
        new_year %= 700
        return jul_add_yyxx(new_year)
    elif cal_type == 'ENGLISH':
        if year >= 1752:
            if year == 1752:
                if month in range(9, 13):
                    if month == 9:
                        if date >= 14:
                            return 0
                        else:
                            return 4
                    else:
                        return 0
                else:
                    return 4
            else:
                new_year = year % 400
                return ce_add_yyxx(new_year)
        else:
            new_year = year
            if year < 0:
                new_year = (year + 1) % 700
            new_year %= 700
            return jul_add_yyxx(new_year)
    elif cal_type == 'ROMAN':
        if year >= 1582:
            if year == 1582:
                if month in range(10, 13):
                    if month == 10:
                        if date >= 15:
                            return 3
                        else:
                            return 6
                    else:
                        return 3
                else:
                    return 6
            else:
                new_year = year % 400
                return ce_add_yyxx(new_year)
        else:
            new_year = year
            if year < 0:
                new_year = (year + 1) % 700
            new_year %= 700
            return jul_add_yyxx(new_year)


# Add value calculated from the year.
def add_year(year, month, date, cal_type):
    return add_yyxx(year, month, date, cal_type) + add_xxyy(year, cal_type)


# Add value for the month based on the year and cal_type.
def add_month(year, month, cal_type):
    if is_leap_year(year, cal_type) and len(MONTH_OFFSET[month - 1]) > 1:
        return MONTH_OFFSET[month - 1][1]
    return MONTH_OFFSET[month - 1][0]


# Returns the day of the week or raises error if a date can't be calculated.
def date(year, month, date, cal_type='ENGLISH'):
    cal_type = cal_type.upper()
    check = is_real_date(year, month, date, cal_type)
    if check == 1:
        total = ((add_year(year, month, date, cal_type) +
                 add_month(year, month, cal_type) + date) % 7)
        return DAYS[total]
    raise Exception("Cannot Calculate Date %s, %s, %s, %s" %
                    (str(year), str(month), str(date), cal_type))
