from cryptography.fernet import Fernet




def szyfrowanie(plik):
    klucz = open(plik, 'r')
    p = klucz.read()
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(bytes(p,'utf-8'))
    zaszyfrowany_plik = open('zaszyfrowane.txt','w')
    zaszyfrowany_plik.write(str(token))
    odkodowane = str(f.decrypt(token))
    odkodowane = odkodowane[2:]
    odkodowane = odkodowane[:-1]
    return odkodowane



