import requests
import sys

Key = "0d1356a0c37774b2f1b132913381d9b1"
url = "https://developers.zomato.com/api/v2.1/"


# funkcja która pobiera ewentualny kod błędu strony
def zwracany_kod(x):
    if x == 404:
        return "Nie ma żadnych restauracji wspieranych przez Zomato  obok wskazanego miejsca"
    elif x == 440:
        return 'Wygasł limit klucza Api'
    elif x == 403:
        return 'Nieprawidłowy klucz Api'
    else:
        pass

def funkcja_szer_dlug(szerokosc, dlugosc):
    listaAdresow = []
    headers = {'Accept': 'application/json', 'user-key': Key}
    r = requests.get(url + "geocode?lat=" + str(szerokosc) + "&lon=" + str(dlugosc), headers=headers)
    # kod który zwraca request
    kod = r.status_code
    try:
        dane = r.json()
    #przypisanie do listy potrzebmych dla nas danych
        for x in dane['nearby_restaurants']:
            listaAdresow.append((x['restaurant']['location']['latitude']))
            listaAdresow.append((x['restaurant']['location']['longitude']))
            listaAdresow.append((x['restaurant']['name']))
            listaAdresow.append((x['restaurant']['user_rating']['aggregate_rating']))
            listaAdresow.append((x['restaurant']['menu_url']))
    except:
        return  zwracany_kod(kod)
    return listaAdresow

def funkcja_miasto_na_miasto_id(miasto):
    zbior =[]
    headers = {'Accept': 'application/json', 'user-key': Key}
    r = requests.get(url + 'locations?query='+ str(miasto), headers=headers)
    kod = r.status_code
    dane = r.json()
    szerokosc = (dane['location_suggestions'][0]['latitude'])
    dlugosc =(dane['location_suggestions'][0]['longitude'])
    szerokosc1=szerokosc
    dlugosc1  = dlugosc
    #rozszerzenie wyszukania restauracji
    for x in range(5):
        zbior.append(szerokosc)
        zbior.append(dlugosc)
        szerokosc+=0.01
        dlugosc += 0.01
        szerokosc1 -=0.01
        dlugosc1 -= 0.01
    return zbior

