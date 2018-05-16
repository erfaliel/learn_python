# programme calculant années bisextiles
annee = input("Enrtrez une année : ")
annee = int(annee) # convertir en entier

if (annee % 4 ) != 0:
  bisextile = False
elif (annee % 100) != 0:
  bisextile = True
elif (annee % 400) == 0:
  bisextile = True
else:
  bisextile = False

# on affiche le résultat
if bisextile == True:
  print(annee, " est une année bisextile.")
else:
  print(annee, " n'est pas une année bisextile")