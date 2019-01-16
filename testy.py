from unittest import TestCase
from polaczenie import wynik
from lokalizacja import zwracany_kod,funkcja_szer_dlug,funkcja_miasto_na_miasto_id,search


class FlaskTest(TestCase):

    def test_greeting(self):
        self.app.get('/')
        self.assert_template_used('index.html')


class LokalizacjaTest(TestCase):
    def test_zwracany_kod(self):
        x = 404
        assert zwracany_kod(
            x) == "Nie ma żadnych restauracji wspieranych przez Zomato  obok wskazanego miejsca", "Błąd aplikacji"
        x = 440
        assert zwracany_kod(
            x) == 'Wygasł limit klucza Api',"Błąd aplikacji"
        x = 403
        assert zwracany_kod(
            x) == 'Nieprawidłowy klucz Api',"Błąd aplikacji"
    def test_funkcja_szerokosc_dlugosc(self):
        x = funkcja_szer_dlug(20.23,23.23)
        assert type(x) == list ,TypeError
        x = funkcja_szer_dlug("ddd", 23.23)
        assert type(x) == list, TypeError


