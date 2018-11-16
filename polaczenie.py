from flask import Flask,render_template,request
from lokalizacja import funkcja_szer_dlug

import webbrowser

app = Flask(__name__,template_folder='Strona')

webbrowser.open_new_tab("http://127.0.0.1:5000")
@app.route('/wynik',methods=['POST'])
def wynik():
    szerokosc = request.form['szerokosc']
    dlugosc = request.form['dlugosc']
    zasieg = request.form['zasieg']

    return funkcja_szer_dlug(szerokosc,dlugosc,zasieg)
    #return render_template("wynik.html")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
