from cryptography.fernet import Fernet
klucz=open('klucz.txt','r').read()
key = Fernet.generate_key()
# Put this somewhere safe!
def szyfrowanie(klucz):
    f = Fernet(key)
    token = f.encrypt(b"klucz")
    print(f)

def deszyfrowanie():
    odkodowane = f.decrypt(token)
    return odkodowane
'A really secret message. Not for prying eyes.'

szyfrowanie(klucz)