# -*-coding:utf-8 -*
numerateur   = input("Entrez un numérateur : ")
denominateur = input ("Entrez un dénominateur : ")

# Vérification des valeurs
try:
  numerateur   = int(numerateur)
  denominateur = int(denominateur)
except ValueError:
  try:
    numerateur   = float(numerateur)
    denominateur = float(denominateur)
  except:
    print("Une des valeurs saisies n'est pas un nombre.")
# Calcul de la division si réalisable.
try:
  resultat = numerateur / denominateur
except NameError:
  print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
  print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
  print("La variable denominateur est égale à 0.")
except ValueError:
  print("Une des valeurs saisies n'est pas un entier.")
else:
  print("Le résultat obtenu est ", resultat)
finally:
  print("fin de programme.")
  #finally est optionnel est permet de lancer des instructions quelque 
  #soit le résultat, même avec des erreurs. 