import random


def generate_date():
    year = random.randint(1900, 2023)
    month = random.randint(1, 12)
    if month < 9:
        month = "0" + str(month)
    monthList = ["01", "03", "05", "07", "08", "10", "12"]
    if month == "02":
        day = random.randint(1, 28)
    elif month in monthList:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    if day < 9:
        day = "0" + str(day)
    date = str(day) + str(month) + str(year)
    return date


def generate_daycounter():
    daycounter = random.randint(1, 998)
    if daycounter < 9:
        daycounter = "00" + str(daycounter)
    elif daycounter < 100:
        daycounter = "0" + str(daycounter)
    return daycounter


def validate_date(date):
    monthList = ["01", "03", "05", "07", "08", "10", "12"]
    if len(date) != 8:
        print("Invalid date")
        date = ""
    else:
        day = date[0:2]
        month = date[2:4]
        genZ = date[4:5]
        year = date[6:8]
        completeYear = date[4:8]
        if int(month) > 12 or int(month) == 0:
            print("There are only 12 months in a year.")
        elif int(completeYear) < 1900:
            print("Date is too old.")
        elif int(month) == 2 and int(day) > 28:
            print("Only 28 days in February.")
        elif month not in monthList and int(day) > 30:
            print("Only 30 days in that month.")
        else:
            if int(genZ) == 2:
                year = genZ + year
            date = year + month + day
    return date


def generate_insz(date):
    # Removing symbols out of the input
    symbols = "/-."
    for symbol in symbols:
        date = date.replace(symbol, "")
    # Generating a date if none is given
    if date == "":
        date = generate_date()
    # Validating if the date is a correct one
    date = str(validate_date(date))
    if len(date) == 6 or len(date) == 7:
        # Generating a daycounter
        daycounter = str(generate_daycounter())
        inszNr = date + daycounter
        # Calculating the last two digits
        checkdigit = 97 - (int(inszNr) % 97)
        if checkdigit < 9:
            checkdigit = "0" + str(checkdigit)
        inszNr = inszNr + str(checkdigit)
        # Removing the additional number in case someone was born after 2000's
        if len(inszNr) == 12:
            inszNr = inszNr[1:12]
        return inszNr
    else:
        return "Please supply a correct date."


print("Input a date or press enter")
inputDate = input()
print(generate_insz(inputDate))
