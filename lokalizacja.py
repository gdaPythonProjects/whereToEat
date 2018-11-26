import requests

Key = "b1216d51234f336579b6aed812325d24"
Key1="TFpFrRxkN4mshvr9bKNn0JkGwl9Fp1Mir8UjsnIpACinjydvjm"

# funkcja która pobiera dane z API
def funkcja_szer_dlug(szerokosc, dlugosc, zasieg):
    listaMiejsce = []
    listaAdresow = []

    url = "https://developers.zomato.com/api/v2.1/search?lat=" + str(dlugosc) + "&lon=" + str(
        szerokosc) + "&sort=real_distance"
    r = requests.get(url, headers={'user-key': Key})
    data = r.json()
    miejsca = data['restaurants']
    # Wejście do JSON'A
    for miejsce in miejsca:
        listaAdresow.append((miejsce['restaurant']['location']['latitude']))
        listaAdresow.append((miejsce['restaurant']['location']['longitude']))
        listaAdresow.append((miejsce['restaurant']['name']))
        listaAdresow.append((miejsce['restaurant']['user_rating']['aggregate_rating']))
        listaAdresow.append((miejsce['restaurant']['menu_url']))

    # poukladane1 = "<br />".join(listaAdresow)
    return listaAdresow
def funkcja_miasto():
    listaMiejsce = []
    url = "https://hoppit.p.mashape.com/getPlaces"
    r = requests.get(url, headers={"X-Mashape-Key": Key1})
    data = r.json()

    print(str(data))
