#chaine -> liste
ma_chaine = "Bonjour à tous"
ma_chaine.split(" ")

#liste -> chaine
ma_chaine = ['Bonjour', 'à', 'tous']
" ".join(ma_chaine)

# but de l'exercice:
"""
>>> afficher_flottant(3.99999999999998)
'3,999'
>>> afficher_flottant(1.5)
'1,5'
>>>"""
def afficher_flottant(flottant):
  """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères 
     représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.
     De plus, on va remplacer le point décimal par la virgule"""
  if type(flottant) is not float:
    raise TypeError("C'est un nombre décimal qui doit être saisi.")
  partie_entiere, partie_flottante = str(flottant).split(".")
  return ",".join([partie_entiere,partie_flottante[:3]])

print("afficher le flotant {} avec la virgule et réduit à 3 digits : "
  .format(afficher_flottant(3.999998)))
####################################################
#Fonction avec un nombre de paramètres indéterminés:
####################################################
def fonction_inconnue(*parametres):
  """Test d'une fonction pouvnant être appelée avec un nombre
     varible de paramètres. """
  print("j'ai reçu : {}.".format(parametres))

fonction_inconnue()
fonction_inconnue(23)
fonction_inconnue('a', 'e', 'f', [4])
# À noter que les parametres sont traités sous la forme d'un tuple.
# on peut placer en tête des paramètres obligatoires:
def fonction_inconnue2(prenom, nom, *parametres):
  """Test d'une fonction pouvnant être appelée avec un nombre
     varible de paramètres. """
  print("{} {}, j'ai reçu : {}.".format(prenom, nom, parametres))

fonction_inconnue2("vincent", "garcia")
fonction_inconnue2("vincent", "garcia", 33)
fonction_inconnue2("vincent", "garcia", 'a', 'e', 'f', [4])

# on place les paramètres nommés en queue…
def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargée de reproduire le comportement de print.
    
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :

    print(chaine, end='')"""
    
    # Les paramètres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaîne
    # Sinon on va avoir quelques problèmes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des paramètres ne contient plus que des chaînes de caractères
    # À présent on va constituer la chaîne finale
    chaine = sep.join(parametres)
    # On ajoute le paramètre fin à la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')

afficher('on', 'écrit', 'une', 'phrase')
afficher('on', 'écrit', 'une', 'phrase', sep='_')
afficher('on', 'écrit', 'une', 'phrase', fin='.')

###################################################
#Transformer une liste en paramètres de fonction
###################################################
# C'est le contraire du pargraphe précédent
liste_des_parametres = [1, 4, 9, 16, 25, 36]
print(*liste_des_parametres)
#>>> 1 4 9 16 25 36
"""Ce qu'il faut retenir si le *variable est dans 
la définition d'une fonction -> cela indique que l'on attend un tuple
de paramètre, c'est à dire un nombre de paramètres inconnu.liste_des_parametres
Si *variable est passé en paramètre d'une fonction ->
la variable sera décomposée en plusieurs paramètres envoyés à la
fonction"""

###################################################
#Les compréhensions de liste
###################################################
# sont un moyen de filtrer ou modifier une liste très simplement.
# parcours simple
liste_origine = [0, 1, 2, 3, 4, 5]
print([nb * 2 for nb in liste_origine])
print([nb * nb for nb in liste_origine])
# parcours avec guards
liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([nb for nb in liste_origine if nb%2 == 0])

# parcours mixte
quantite_a_retirer = 7
stockes = [15, 3, 18, 21]
print(
  [
    nb_produit - quantite_a_retirer for nb_produit in stockes 
    if nb_produit > quantite_a_retirer
 ])

#Trier cette liste 
stockes = [
  ('fraises', 76),
  ('prunes',  51),
  ('pommes',  22),
  ('poires',  18),
  ('melons',   4),
]

# on inverse quantité et fruits
stockes_trie_inverse = [(quantite, fruit) for (fruit, quantite) in stockes]
#stockes_trie_inverse = sorted(stockes) # version fonctionnelle
stockes_trie_inverse.sort(reverse = True) # Version méthode de l'objet liste
print(stockes_trie_inverse)
stockes_trie = [(fruit, quantite) for (quantite, fruit) in stockes_trie_inverse]
print(stockes_trie)

# Boucle inverse
for i in reversed(range(1, 2, 10)):
  print(i)

# la fonction Zip
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print('What is your {0}?  It is {1}.'.format(q, a))




