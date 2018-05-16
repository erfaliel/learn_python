# programme calculant années bisextiles
annee = input("Enrtrez une année : ")
annee = int(annee) # convertir en entier

if annee % 400 == 0 or (annee % 4 == 0 and annee %100 != 0):
  print(annee, " est une année bisextile.")
else:
  print(annee, " n'est pas une année bisextile")