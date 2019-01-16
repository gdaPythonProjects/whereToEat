from cryptography.fernet import Fernet
# Put this somewhere safe!
def szyfrowanie():
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"costam cosdtam")
    print(token)

def deszyfrowanie():
    odkodowane = f.decrypt(token)
    return odkodowane
'A really secret message. Not for prying eyes.'