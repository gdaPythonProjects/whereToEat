from flask import Flask,render_template,request
from lokalizacja import funkcja_szer_dlug
import webbrowser
#postawienie sewera
app = Flask(__name__,template_folder='Strona')

@app.route('/wynik',methods=['POST'])
def wynik():
    szerokosc = request.form['szerokosc']
    dlugosc = request.form['dlugosc']
    zasieg = request.form['zasieg']
    #x jest potrzebny do skrócenia nazwy funkcji
    x = funkcja_szer_dlug(szerokosc,dlugosc,zasieg)
    #wysłanie danych do wynik.html
    return funkcja_szer_dlug(szerokosc,dlugosc,zasieg)
    #return render_template("wynik.html",przeslij_html=x)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    webbrowser.open_new("http://127.0.0.1:5000")
    app.run(debug=False)


