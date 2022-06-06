import os

path = os.getcwd()
print (path)
print()

from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

dayStart = int(input("Dia Inical (D) "))
dayEnd = int(input("Dia Final (D) "))
month = int(input("Mês (MM) "))
year = int(input("Ano (AAAA) "))

start_dt = date(year, month, dayStart)
end_dt = date(year, month, dayEnd)
for dt in daterange(start_dt, end_dt):
    whatever = dt.strftime("%d-%m-%Y")
    print(whatever)
    
    try:
       os.makedirs(whatever)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s" % path)
