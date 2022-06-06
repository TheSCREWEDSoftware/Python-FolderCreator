#main.py
#Author: Augusto Mendes
#E-mail: augustomendes4426[at]gmail.com
#Version 2

import os

def messages(x):
    print("")
    if x == 0: # Days
        print("Use a valid full-number")
        print("and Within the days of the month\n")

    if x == 1: # Month
        print("Use a valid full-number")
        print("and Within the months of the year\n")

    if x == 2: # Year
        print("Use a valid full-number")
        print("and A valid year \n")


path = os.getcwd()
print(path)
print()

iceBreaker = 1 # This stops the Loop of the Inputs (1 = Enabled, 0 = Disabled)

from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + timedelta(n)

while iceBreaker == 1:
    try:
        dayStart = int(input("Starting Day (D) ")) # D/DD
        dayStartCheck = date(1, 1, dayStart)
        
    except ValueError as a:
        #print(a)
        messages(0)
             
    else:
        while iceBreaker == 1:
            try:
                dayEnd = int(input("Ending Day (D) ")) # D/DD
                dayEndCheck = date(1, 1, dayEnd)

            except ValueError as b:
                #print(b)
                messages(0)
                
            else:
                while iceBreaker == 1:
                    try:
                        month = int(input("Month (MM) ")) # M/MM
                        monthCheck = date(1, month, 1)

                    except ValueError as c:
                        #print(c)
                        messages(1)

                    else:
                        while iceBreaker == 1:
                            try:
                                year = int(input("Year (YYYY) ")) # YYYY
                                yearCheck = date(year, 1, 1)
                                
                            except ValueError as d:
                                #print(d)
                                messages(2)

                            else:
                                iceBreaker = 0
print("")

dateStart = date(year, month, dayStart)
dateEnd = date(year, month, dayEnd)

for dateIndex in daterange(dateStart, dateEnd):
    dateFinal = dateIndex.strftime("%d-%m-%Y") #DAY (D/DD) - MONTH (M/MM) - YEAR (YYYY)
    print("\n"+dateFinal+"\n")

    try:
        os.makedirs(dateFinal)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)

input("\nPress any key to exit ")
