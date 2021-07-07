# find what the day is on that date.
# input format MM DD YYYY

from calendar import monthcalendar, setfirstweekday, MONDAY, day_name

m, d, y = map(int, input().split())
setfirstweekday(MONDAY)

month = monthcalendar(y,m)
for w in month:
    if d in w:
        strDay = list(day_name)[w.index(d)]
        print(strDay.upper())
    