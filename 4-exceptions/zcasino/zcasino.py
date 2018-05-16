from math   import ceil
from random import randrange


solde = 49 # mise de départ (le nombre max)

def is_odd(nombre):
  if nombre % 2 == 0:
    return "Pair"
  else:
    return "Impair"

def get_a_number(max):
  if max > 49:
    max = 49
  try:
    nombre = input("Saisir une valeur entre 0 et max , cela sera également votre mise : ")
    nombre = int(nombre)
    print("TRACE-get_a_number, type : ", type(nombre), "max vaut: ", max)
    assert (nombre > 0 and nombre <= max)
  except ValueError:
    print("Vous n'avez pas saisi un nombre.")
    get_a_number(max)
  except AssertionError:
    print("La valeur saisie n'est pas dans le scope autorisé.")
    get_a_number(max)
  else:
    return nombre

# Lancement du jeu.
max = solde
tour = 0
while solde > 0:
  # Saisie du nombre et de la mise
  nombre = get_a_number(max)
  mise = nombre
  print("TRACE: ", type(nombre))
  nbr_roue = randrange(50)
  pair_nbr_roue = is_odd(nbr_roue)
  pair_nombre = is_odd(nombre)

  print("Le n° ", nbr_roue, " est ", pair_nbr_roue, " votre numéro est le ", nombre)

  if nbr_roue == nombre:
    solde += mise * 3
  elif pair_nbr_roue == pair_nombre:
    solde += ceil(mise/2)
  else:
    solde -= mise
  tour += 1
  print("Tour n°", tour)
  print("votre solde est de : ", solde)
  #max = solde
print("Vous avez perdu !")
