import requests

Key ="0d1356a0c37774b2f1b132913381d9b1"
#funkcja która pobiera dane z API
def funkcja_szer_dlug(szerokosc,dlugosc,zasieg):
    listaMiejsce=[]
    listaAdresow=[]

    url1 = "https://developers.zomato.com/api/v2.1/search?count=100&lat="+str(dlugosc)+"&lon="+str(szerokosc)+"&radius="+zasieg+"&sort=real_distance"
    r = requests.get(url1, headers={'user-key': Key})
    data =r.json()
    miejsca = data['restaurants']
    #Wejście do JSON'A
    for miejsce in miejsca:
        listaMiejsce.append(str(miejsce['restaurant']['name']))
        listaAdresow.append(str(miejsce['restaurant']['location']['address']))


    poukladane1 = "<br />".join(listaMiejsce)
    poukladane2 = "<br />".join(listaAdresow)
    return poukladane1