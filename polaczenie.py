from flask import Flask, render_template, request
from lokalizacja import funkcja_szer_dlug,funkcja_miasto_na_miasto_id,funkcja_miasto
import webbrowser

# postawienie sewera
app = Flask(__name__, template_folder='Strona')


@app.route('/wynik', methods=['POST'])
def wynik():
    szerokosc = request.form['szerokosc']
    dlugosc = request.form['dlugosc']
    miasto = request.form['miasto']


    # wysłanie danych do wynik.html
    if szerokosc == '' or dlugosc == '':
        s, d = funkcja_miasto_na_miasto_id(miasto)
        y = funkcja_miasto(50,s,d)
        if type(y) == list:
            return render_template("wynik.html", przeslij_html=y)
        elif type(y) == str:
            return y
        else:
            return "Nieznany błąd"
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
