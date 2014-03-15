__version__ = '2.0.0'
__author__ = 'Violet (PariahVi)'

month_offset = ([4, 3], [0, 6], [0], [3], [5], [1], [3], [6], [2], [4], [0],
                [2])
days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday')
types = ('GREGORIAN', 'CE', 'JULIAN', 'ENGLISH', 'ROMAN')
month_names = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')


def ce_leap_year(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return 1
    elif y % 4 == 0:
        return 1
    return 0


def jul_leap_year(y, ny):
    if y < 0:
        ny = (y + 1) % 700
    if ny % 4 == 0:
        return 1
    return 0


def is_leap_year(year, type):
    if type == "GREGORIAN":
        new_year = year
        if year < 0:
            new_year = (year + 1) % 400
        return ce_leap_year(new_year)
    if type == "CE":
        return ce_leap_year(year)
    if type == "JULIAN":
        new_year = year
        jul_leap_year(year, new_year)
    if type == "ENGLISH":
        new_year = year
        if year >= 1800:
            return ce_leap_year(new_year)
        elif year < 1800:
            return jul_leap_year(year, new_year)
    if type == "ROMAN":
        new_year = year
        if year >= 1700:
            return ce_leap_year(new_year)
        elif year < 1700:
            return jul_leap_year(year, new_year)


def check_int(value):
    try:
        int(value)
    except ValueError:
        return 0
    return 1


def is_real_date(year, month, date, type):
    month30 = (4, 6, 9, 11)
    if month not in range(1, 13):
        return 2
    if not check_int(year):
        return 3
    if not check_int(date) or date < 1 or date > 31:
        return 4
    if type not in types:
        return 5
    if not year and type != "CE":
        return 6
    else:
        if month in month30 and date > 30:
            return 7
        elif month == 1 and not (date < 29 or (is_leap_year(year, type)
                                 and date == 29)):
            return 7
    if type == "ENGLISH":
        if month == 9 and date > 2 and date < 15 and year == 1752:
            return 8
    if type == "ROMAN":
        if month == 10 and date > 4 and date < 16 and year == 1582:
            return 8
    return 1


def add_xxyy(year, type):
    if type != "CE":
        if year < 0:
            new_year = (year + 1) % 100
        else:
            new_year = year % 100
    else:
        new_year = year % 100
    return ((int(new_year / 12) + (new_year % 12) +
            int((new_year % 12) / 4)) % 7)


def ce_add_yyxx(y):
    yyxx = (2, 0, 5, 3)
    return yyxx[int(y / 100) % 4]


def jul_add_yyxx(y):
    return (7 - int(y / 100)) % 7
    if y < 100:
        return 0
    else:
        return 7 - int(y / 100)


def add_yyxx(year, month, date, type):
    if type == "GREGORIAN":
        new_year = year
        if year < 0:
            new_year = (year + 1) % 400
        new_year = new_year % 400
        return ce_add_yyxx(new_year)
    if type == "CE":
        new_year = year % 400
        return ce_add_yyxx(new_year)
    if type == "JULIAN":
        new_year = year
        if year < 0:
            new_year = (year + 1) % 700
        new_year = new_year % 700
        return jul_add_yyxx(new_year)
    if type == "ENGLISH":
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
            new_year = new_year % 700
            return jul_add_yyxx(new_year)
    if type == "ROMAN":
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
            new_year = new_value % 700
            return jul_add_yyxx(new_year)


def add_year(year, month, date, type):
    return add_yyxx(year, month, date, type) + add_xxyy(year, type)


def add_month(year, month, type):
    if is_leap_year(year, type) == 1 and len(month_offset[month - 1]) > 1:
        return month_offset[month - 1][1]
    return month_offset[month - 1][0]


def date(year, month, date, type='ENGLISH'):
    month_name = month_names[month - 1]
    type = type.upper()
    check = is_real_date(year, month, date, type)
    if check == 1:
        total = ((add_year(year, month, date, type) +
                 add_month(year, month, type) + date) % 7)
        return days[total]
    if type != 'CE':
        type = type.capitalize()
    exceptions = {
        2: 'Expected integer between 1 and 12 for month',
        3: 'Expected integer for year',
        4: 'Expected integer between 1 and 31 for date',
        5: '%s is not an available calendar type' % (type),
        6: 'The %s Calendar does not have a year %s' % (type, str(year)),
        7: '%s does not have %s days in it' % (month_name, str(date)),
        8: 'The %s Calendar did not have that date' % (type)
    }
    if check in range(2, 9):
        raise Exception(exceptions[check])
