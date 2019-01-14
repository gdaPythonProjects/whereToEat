from flask import Flask, render_template, request
from lokalizacja import funkcja_szer_dlug,funkcja_miasto_na_miasto_id
import webbrowser

# postawienie sewera
app = Flask(__name__, template_folder='Strona')


@app.route('/wynik', methods=['POST'])
def wynik():
    szerokosc = request.form['szerokosc']
    dlugosc = request.form['dlugosc']
    miasto = request.form['miasto']


    # zapytanie o miasto

    if szerokosc == '' or dlugosc == '':
        y= []
        s = funkcja_miasto_na_miasto_id(miasto)
        sz = [x for x in s if s.index(x)%2==0]
        dl = [x for x in s if s.index(x)%2!=0]
        for x in range(len(sz)):
            y.append(funkcja_szer_dlug(sz[x],dl[x]))
        nowa_lista = []
        for x in range(0,len(y)):
            nowa_lista +=y[x]
        if type(y) == list:
            return render_template("wynik.html", przeslij_html=nowa_lista)
        elif type(y) == str:
            return y
        else:
            return "Nieznany błąd"
    #zapytanie o długosć i szerokość geograficzną
    else:
        x = funkcja_szer_dlug(szerokosc, dlugosc)
        if type(x) == list:
            return render_template("wynik.html", przeslij_html=x)
        elif type(x) == str:
            return x
        else:
            return "Nieznany błąd"


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    webbrowser.open_new("http://127.0.0.1:5000")
    app.run(debug=False)
