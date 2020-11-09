##********************************************************************
## PROGRAM NAME:    	Lab6.py
## AUTHOR:          	Thad W. Turner
## DATE:   	            10/2/2020
## PURPOSE:         	To calculate the day of the week for a given date
##                  	from a file dates.txt in the working directory.
##********************************************************************
##
######################################################################
##                                                                  ##
##                            FUNCTIONS                             ##
##                                                                  ## 
######################################################################
##
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## FUNCTION:	isLeapYear			         
## PURPOSE:	    Returns True if the year is a leap year
##              Otherwise, returns False
##
## INPUT:       year (int)
## OUTPUT:      leapYear (boolean)
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def isLeapYear(year):
    if (year%4 == 0) and ((year%100 !=0) or (year%400 == 0)):
        leapYear = True            
    else:
        leapYear = False

    return leapYear

##END OF FUNCTION isLeapYear
##
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## FUNCTION:	isValidDate			         
## PURPOSE:	    Returns True if the date is valid; otherwise False 
##
## INPUT:       year (int)
##              month (int)
##              day (int)
##
## OUTPUT:      validDate (boolean)
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def isValidDate(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    validDate = False
    if year >= 1752 and year <= 2399:
        if day >= 1:
            if month in [1,3,5,7,8,10,12] and day <= 31:
                validDate = True
            elif month in [4,6,9,11] and day <= 30:
                validDate = True
            elif month == 2:
                if isLeapYear(year) and day <= 29:
                    validDate = True
                elif not isLeapYear(year) and day <= 28:
                    validDate = True
                    
    return validDate

##END OF FUNCTION isValidDate
##
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## FUNCTION:	calcDayOfWeek		         
## PURPOSE:	    Calculates and returns the integer representing the 
##              day fo the week. Sunday = 0; Saturday = 6.
##
## INPUT:       yearCode (int), monthCode (int), centuryCode (int), 
##              dayNumber (int), leapYearCode (int)
##
## OUTPUT:      dow (int)
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def calcDayOfWeek(yearCode, monthCode, centuryCode, dayNumber, leapYearCode):
    dow = (yearCode + monthCode + centuryCode + dayNumber - leapYearCode) % 7
    return dow

##END OF FUNCTION isValidDate    
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## FUNCTION:	getLeapYearCode		         
## PURPOSE:	    Returns an adjustment needed January and February in 
##              leap years.
##
## INPUT:       year (int), month (int)
##
## OUTPUT:      leapYearCode (int)
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def getLeapYearCode(year, month):
    if (month == 1 or month == 2) and (isLeapYear(year) == True):
        leapYearCode = 1
    else:
        leapYearCode = 0
    return leapYearCode

##END OF FUNCTION isValidDate

######################################################################
##                                                                  ##
##                               MAIN                               ##
##                                                                  ## 
######################################################################
##LISTS
## MonthCodeList elements are ["January","February","March","April","June","July","August","September","October","November","December"]
monthCodeList = [0,3,3,6,1,4,6,2,5,0,3,5]
## centuryCodeList elements are [1700, 1800, 1900, 2000, 2100, 2200, 2300]
centuryCodeList = [4,2,0,6,4,2,0]
dayName = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",]
longMonthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

## Introductory prints to show program
print("-------  Day of the Week Calculator -------")
print("      Reading dates in from dates.txt..")
print()

## Read a date from the data file dates.txt
fname = open('dates.txt','r')
record = fname.readline()
dates = []
while record != "":                 #Loop while not at end of file
    record = record.rstrip("\n")    #Strip new line control character
    ## Check to make sure it is integers, accept date in the form of YYYYMMDD between 1752-2399 inclusive.
    ##Try to get the first four digits to make sure it is an int and if not then say invalid date and don't add to array
    try:
        if int(str(record)[:4]) >= 1752 or int(str(record)[:4]) <= 2399 and (len(str(record)) == 8): ## If rules are met record is put into list.
            dates.append(str(record))
    except:
        try:
            if int(str(record)[:4]) <= 1752 or int(str(record)[:4]) >= 2399:
                print(record + " is not a date in the valid range.")
            if len(record) != 8:
                print(record + " must be eight charecters long.")
            if int(record) < 0:
                print(record + " must be a positive integer.")
            ## If statements for different types of issues with the input
        except:
            print(record + " is not an integer.")
    finally:
        record = fname.readline()
## Close file and print list of dates
fname.close()
print("Here are your dates: ")
## For each element in list split, validate, if valid then do rest of calcs, if not valid then display message and move on
for date in dates:
    ## Split the date into corresponding integer components
    yearNum = date[0:4]
    monthNum = date[4:6]
    dayNum = date[6:]
    centuryNum = date[0:2]
    shortYearNum = date[2:4]
    ## print(yearNum, monthNum, dayNum, centuryNum, shortYearNum,)
    ## Validate date entered (isValidDate function)
    ## If not valid show a message and then go to next date.
    if isValidDate(yearNum, monthNum, dayNum) == False:
        print(monthNum + "/" + dayNum + "/" + yearNum + " is not a valid date.")
    else:
        ## If valid then move on to other operations
        ## Calc the yearcode (YY + (YY/4)%7)
        yearcode = ((int(shortYearNum) + (int(shortYearNum)/4))%7)
        ## Retrieve month code from monthCodeList[]
        monthCode = monthCodeList[int(monthNum)-1]
        ## Get Century Code from the list. 
        centuryCode = 0
        if int(centuryNum) == 17:
            centuryCode = centuryCodeList[0]
        elif int(centuryNum) == 18:
            centuryCode = centuryCodeList[1]
        elif int(centuryNum) == 19:
            centuryCode = centuryCodeList[2]
        elif int(centuryNum) == 20:
            centuryCode = centuryCodeList[3]
        elif int(centuryNum) == 21:
            centuryCode = centuryCodeList[4]
        elif int(centuryNum) == 22:
            centuryCode = centuryCodeList[5]
        elif int(centuryNum) == 23:
            centuryCode = centuryCodeList[6]
        ## Use getLeapYearCode to get year code
        leapYearCode = getLeapYearCode(yearNum, monthNum)
        ## Use calcDayOfWeek to retrieve the integer day of the week
        dayInt = calcDayOfWeek(yearcode, monthCode, centuryCode, int(dayNum), leapYearCode,)
        ## Use the day of week list to get the day name then print result
        print(longMonthNames[int(monthNum) - 1] + " " + str(int(dayNum)) + ", " + yearNum + " was a " + dayName[int(dayInt)])
## End of program message
print("\nAll dates have been processed.")
input("Press enter to close.")
##END OF MAIN