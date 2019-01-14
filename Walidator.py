import re
def dzialanie_na_stringu(dane):
    x = re.compile('[a-zA-Zńąęćółśźż]+')
    dane = x.findall(dane)
    print(str(''.join(dane)))
def dzialanie_na_liczbie(liczba):
    liczba = liczba.replace(',', '.')
    x=re.compile(r"[+-]?\d{1,2}\.?\d*")
    liczba = x.findall(liczba)
    print(liczba)
dzialanie_na_liczbie("dd5g-e,.,.,.,.,.,.,.#@3.213d")