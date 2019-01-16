from cryptography.fernet import Fernet
klucz=open('klucz.txt','r').read()
key = Fernet.generate_key()
# Put this somewhere safe!
def szyfrowanie():
    f = Fernet(key)
    token = f.encrypt(klucz)
    print(token)

def deszyfrowanie():
    odkodowane = f.decrypt(token)
    return odkodowane
'A really secret message. Not for prying eyes.'

szyfrowanie();