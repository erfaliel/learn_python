chaine = str() # Crée une chaine de caractère
# On obtient le même résultat avec chaine = ""

while chaine.lower() != "q":
  print("Tapez 'Q' pour quitter…")
  chaine = input()
  print("chaine vaut : ", chaine)

print("merci !")