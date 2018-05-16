# méthode str.format
prenom = "Paul"
nom = "Dupont"
age = "21"

nouvelle_chaine = "Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age)
print(nouvelle_chaine)

print( \
  "Je m'appelle {0} {1} ({3} {0} pour l'adiministration) et j'ai {2} " \
  "ans.".format(prenom, nom, age, nom.upper()))

# À noter que la numérotation est optionel, dans ce cas par exemple:
# Cela implique alors que les variables soient dans l'ordre.
date = "Dimanche 24 juillet 2011"
heure = "17:00"
print("Cela s'est produit le {}, à {}.".format(date, heure))

# Utilisation de format par indice:
adresse = """
{no_rue}, {nom_rue}
<> {code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)

# Concaténation:
prenom          = "Paul"
message         = "Bonjour"
chaine_complete = message + " " + prenom
print(chaine_complete)

age     = 21
message = "J'ai " + str(age) + " ans."
print(message)

# Parcourir des chaines
# 1 # par indice
chaine = "Salut les ZEROS !"
print(chaine[0] + chaine[-1])
# longuer de la chaine
len(chaine) # len est un gestion de sequence qui ne gère pas que les str.

i = 0
while i < len(chaine):
  print(chaine[i])
  i += 1

# Sélection de chaine
presentation = "salut"
presentation[0:2]
presentation[2:len(presentation)]
# ou
presentation[:2]
presentation[2:]

# plein d'autres méthodes dont:
# count, find, replace …
