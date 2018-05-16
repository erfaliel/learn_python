# parcourir une liste
print("Parcours d'une liste: ")
liste =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elem in liste:
  print(elem)

# parcourir une chaine avec filtre
print("\n Parcours d'une chaine avec filtre: ")
chaine = "Bonjour les ZER0S"
for lettre in chaine:
  if lettre in "AEIOUYaeiouy": # si lettre est une voyelle
    print(lettre)
  else: # Sinon on cache
    print("*")
    # À noter que le 0 de ZER0 est caché.