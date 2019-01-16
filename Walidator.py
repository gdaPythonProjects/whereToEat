import re
from decimal import Decimal
def dzialanie_na_stringu(dane):
    x = re.compile('[a-zA-Zńąęćółśźż]+')
    dane = x.findall(dane)
    return str(''.join(dane))

def dzialanie_na_latitude(liczba):
    liczba = liczba.replace(',', '.')
    if len(liczba) > 11:
        liczba = liczba[:13]
    liczba = Decimal(liczba)
    x=re.compile(r"^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,12})?))$")
    liczba = x.findall(liczba)

    return liczba

def dzialanie_na_longitude(liczba):
    liczba = liczba.replace(',', '.')
    x=re.compile(r"^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,12})?))$")
    liczba = x.findall(liczba)
    return liczba
