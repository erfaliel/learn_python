ma_liste = list() # on instancie un objet liste de la classe list
# également ma_liste = []
type(ma_liste)
#>>> <class 'list'>

ma_liste
#>>> []

# créer une liste non vide
ma_liste = [1, 2, 3, 4, 5]
print(ma_liste)

# une liste peut contenir n'importe quel objet:
ma_liste = [1, 3.5, "une chaine", []]
print(ma_liste)

# Accéder aux éléments d'une liste:
ma_liste = ['c', 'f', 'm']
print(ma_liste)
print(ma_liste[0])
print(ma_liste[2])
ma_liste[1] = 'Z' # On remplace 'f' par 'Z': Les listes sont mutables.
# pour rappel ceci n'est pas possible avec le type str.
print(ma_liste)

# Ajouter des éléments dans une liste.
ma_liste = [1, 2, 3]
ma_liste.append(56)
print(ma_liste)
# encore une différence entre list et str.
# Les méthodes str retourne une nouvelle chaine str
# Les méthodes list ne retourne rien mais modifie l'objet list d'origine.

chaine1 = "une petite phrase"
chaine2 = chaine1.upper()
print(chaine1)
print(chaine2)

liste1 = [1, 5.5, -15]
liste2 = liste1.append(-15)
print(liste1)
print(liste2)

# Insérer un élément dans une liste
ma_liste = ['a', 'b', 'd', 'e']
ma_liste.insert(2, 'c') # on insère 'c' à l'indice 2
print(ma_liste)

# Concaténer des listes
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
ma_liste1.extend(ma_liste2)
print(ma_liste1)
# on peut aussi
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
ma_liste1 + ma_liste2 # on ne mute pas la liste1 ici
print(ma_liste1)
print(ma_liste1 + ma_liste2)
ma_liste1 += ma_liste2 # identique à extend donc mutation.
print(ma_liste1)

# suppression d'éléments dans une liste
# on utilise del qui peut aussi être utilisé sur une variable (objet)
toto = 'tata'
print(toto)
del toto
#print(toto) génère une erreur

ma_liste = [-5, -2, 1, 4, 7, 10]
del ma_liste[0]
print(ma_liste)

# Méthode remove
ma_liste = [30, 31, 31, 32, 33]
ma_liste.remove(31) # retire la première occurence rencontrée.
print(ma_liste)

# parcourir une liste
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0
while i < len(ma_liste):
  print(ma_liste[i])
  i += 1

# parcourir une liste plus optimal
for element in ma_liste:
  print(element)

# parcourir avec enumerate
for i, element in enumerate(ma_liste):
  print("À l'indice {} set trouve {}.".format(i, element))
# pour visualiser
for element in enumerate(ma_liste):
  print(element)

autre_liste = [
  [1, 'a'],
  [4, 'd'],
  [7, 'g'],
  [26, 'z'],
] # On peut étaler une liste sur plusieurs lignes.
for nb, lettre in autre_liste:
  print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))

# Rq: Évitez de parcourir une liste dont la taille évolue en même temps.

# Les Tuples
# un tuple est immuable on ne peut modifier, ajouter ou supprimer
a, b = 3, 4 # Affectation en fait
(a, b) = (3, 4) # c'est idem
a, b = ["a", 2]
# est idem à 
(a, b) = ["a", 2]
# a vaut 'b' et b vaut 2


# permet à une fonction de retourner plusieurs valeurs
def decomposer(entier, divise_par):
  """Cette fonction retourne la partie entière et le reste de
  entier / divise_par"""
  p_e =   entier // divise_par
  reste = entier % divise_par
  return p_e, reste #c'est en fait un tuple.

partie_entiere, reste = decomposer(20, 3)
print(partie_entiere)
print(reste)





