import requests

Key ="b1216d51234f336579b6aed812325d24"
#funkcja która pobiera dane z API
def funkcja_szer_dlug(szerokosc,dlugosc,zasieg):
    listaMiejsce=[]
    listaAdresow=[]

    url1 = "https://developers.zomato.com/api/v2.1/search?count=100&lat="+str(dlugosc)+"&lon="+str(szerokosc)+"&sort=real_distance"
    r = requests.get(url1, headers={'user-key': Key})
    data =r.json()
    miejsca = data['restaurants']
    #Wejście do JSON'A
    for miejsce in miejsca:
        listaAdresow.append((miejsce['restaurant']['location']['latitude']))
        listaAdresow.append((miejsce['restaurant']['location']['longitude']))
        listaAdresow.append((miejsce['restaurant']['name']))
        listaAdresow.append((miejsce['restaurant']['user_rating']['aggregate_rating']))
    #poukladane1 = "<br />".join(listaAdresow)
    return listaAdresow
