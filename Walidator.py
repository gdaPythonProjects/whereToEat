import re
def dzialanie_na_stringu(dane):
    x= re.compile('[a-zA-Zńąęćółśźż]+')
    dane = x.findall(dane)
    print(str(''.join(dane)))
def dzialanie_na_liczbie(liczba):
