from cryptography.fernet import Fernet
klucz=open('klucz.txt','w+')
plik =klucz.read()
key = Fernet.generate_key()
# Put this somewhere safe!
def szyfrowanie(plik):
    f = Fernet(key)
    return (f.encrypt(b"plik"))

def deszyfrowanie():
    odkodowane = f.decrypt(token)
    return odkodowane
'A really secret message. Not for prying eyes.'
klucz.write(str(szyfrowanie(plik)))
