from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"costam cosdtam")
print(token)

odkodowane = f.decrypt(token)
print(odkodowane)
'A really secret message. Not for prying eyes.'