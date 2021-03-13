import hashlib
from getpass import getpass

chaine_mot_de_passe = b"azerty" # b allow to declare binary mode : it's needed to handle password
mot_de_passe_chiffre = hashlib.sha256(chaine_mot_de_passe).hexdigest()   # sha256 -> method to encrypt / hexdigest convert into an hexa str
print("Hash à reconstituer: ", mot_de_passe_chiffre)

verrouille = True
while verrouille:
    entre = getpass("taper le mot de passe : ")
    # We encode to get a bytes type
    print("DEBUG : valeur saisie: {}".format(entre))
    entre = entre.encode() # encode turn str into binary
    print("DEBUG : valeur saisie vers binary: {}".format(entre))
    entre_chiffre = hashlib.sha256(entre).hexdigest()
    print("DEBUG : valeur saisie chiffrée : {}".format(entre_chiffre))
    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print("Mot de passe incorrect")

print("Mot de passe accepté…")