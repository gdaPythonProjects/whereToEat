from flask import Flask, render_template, request
from lokalizacja import funkcja_szer_dlug,funkcja_miasto_na_miasto_id,search
from Walidator import dzialanie_na_stringu,dzialanie_na_latitude,dzialanie_na_longitude
import webbrowser
import html

# postawienie sewera
app = Flask(__name__, template_folder='Strona')


@app.route('/wynik', methods=['POST'])
def wynik():
    szerokosc = request.form['szerokosc']
    dlugosc = request.form['dlugosc']
    miasto = request.form['miasto']


    # zapytanie o miasto
    if szerokosc == '' and dlugosc == '' and miasto == '' or szerokosc != '' and dlugosc != '' and miasto != '' :
        return render_template("index.html",przeslij_html="")
    else:
        if szerokosc == '' and dlugosc == '':
            dzialanie_na_stringu(miasto)
            y = search(funkcja_miasto_na_miasto_id(miasto))
            if type(y) == list:
                return render_template("wynik.html", przeslij_html=y)
            elif type(y) == str:
                return y
            else:
                return "Nieznany błąd"
        #zapytanie o długosć i szerokość geograficzną
        else:
            if szerokosc == '' or dlugosc == '':
                return render_template("index.html", przeslij_html="")
            else:
                if szerokosc != szerokosc.isnumeric() or dlugosc!=dlugosc.isnumeric()
                    return 0
                dzialanie_na_longitude(szerokosc)
                dzialanie_na_latitude(dlugosc)
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
