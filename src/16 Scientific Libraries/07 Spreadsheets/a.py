import calendar, os

def f(iter):
    os.system("clear")
    for date in iter:
        print(date, end=" ")

c = calendar.Calendar()
x = c.yeardayscalendar(2023, 1)
print(type(x))
y = next(x)

f(c.itermonthdates(2023, 1))
f(c.itermonthdays(2023, 1))
f(c.itermonthdays2(2023, 1))
f(c.itermonthdays3(2023, 1))
f(c.itermonthdays4(2023, 1))
f(c.monthdatescalendar(2023, 1))
f(c.monthdays2calendar(2023, 1))
f(c.monthdays2calendar(2023, 1))
f(c.yeardatescalendar(2023, 1))
f(c.yeardayscalendar(2023, 1))
f(c.yeardays2calendar(2023, 1))

