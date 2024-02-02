import sys
import re
import requests as r

def main():
    entry=input("In which date you want to review your currency? (YYYY-MM-DD): ")
    if check_format(entry,"date") != entry:
        sys.exit("Invalid date format")
    else:
        money=input("How much euros do you have? (in numbers): ")
        if money.isdigit() and int(money)>0:
            curr=input("What currency comparison do you want? (3 uppercase letters): ")
            if check_format(curr,"currency") != curr:
                sys.exit("Invalid currency")
            else:
                if curr=="USD":
                    print(f"{euro_to_dollar(int(money),entry)} dollars")
                else:
                    print(f"{euro_to_other_currency(int(money),curr,entry)} units of the especified currency")
        else:
            sys.exit("The mount must be a positive number")


def check_format(s,format):
    valid=("CAD","HKD","ISK","PHP","DKK","HUF","CZK","AUD","RON","SEK","IDR","INR","BRL","RUB","HRK","JPY",
           "THB","CHF","SGD","PLN","BGN","TRY","CNY","NOK","NZD","ZAR","USD","MXN","ILS","GBP","KRW","MYR")
    if format=="date":
        if inp := re.search(r"(\d{4})-(\d{2})-(\d{2})",s):
            if int(inp.group(1))<=2023 and 1<=int(inp.group(2))<=12 and 1<=int(inp.group(3))<=31:
                return s
            else:
                return "Invalid date"
        else:
            return "Date format: YYYY-MM-DD"
    elif format=="currency":
        if inp := re.search(r"([A-Z]{3})",s):
            if inp.group(1) in valid:
                return s
            else:
                return "Invalid currency"
        else:
            return "Format: 3 uppercase letters"
    else:
        return "Invalid format argument to the funtion"


def euro_to_dollar(money,date):
    info=r.get(f"http://api.exchangeratesapi.io/{date}?access_key=75a7d698a2b3eed3aa896cc891cfc3d0&symbols=USD").json()
    return round(money*float(info["rates"]["USD"]),2)


def euro_to_other_currency(money,currency,date):
    info=r.get(f"http://api.exchangeratesapi.io/{date}?access_key=75a7d698a2b3eed3aa896cc891cfc3d0&symbols={currency}").json()
    return round(money*float(info["rates"][currency]),2)


if __name__ == "__main__":
    main()