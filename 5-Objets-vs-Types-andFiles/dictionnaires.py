# Créer un dictionnnaire
mon_dictionnaire = dict()
print(type(mon_dictionnaire))
print(mon_dictionnaire)

# Ajouter des clés
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
print(mon_dictionnaire)

# Modifier une clé
mon_dictionnaire["pseudo"] = "6pri1"
print(mon_dictionnaire)

# Accéder à une valeur
print(mon_dictionnaire["mot de passe"])

# les clés peuvent être des entiers
mon_dictionnaire = {}
mon_dictionnaire[0] = "a"
mon_dictionnaire[1] = "e"
mon_dictionnaire[2] = "i"
mon_dictionnaire[3] = "o"
mon_dictionnaire[4] = "u"
mon_dictionnaire[5] = "y"
print(mon_dictionnaire)
# cela ressemble à une liste, mais le fonctionnement n'est
# pas le même: Si l'on supprime un enregistrement, pas de décalage
# automatique de l'indice.
# tous les types sont utilisables commes clé et comme valeur
# Exemple de l'échiquier
echiquier = {}
echiquier[('a', 1)] = "tour blanche"
echiquier[('b', 1)] = "cavalier blanc"
echiquier[('c', 1)] = "fou blanc"
echiquier[('d', 1)] = "reine blanc"
#
echiquier[('a', 2)] = "pion blanc"
echiquier[('b', 2)] = "pion blanc"
print(echiquier) 

# Affecter des clés/valeurs à la déclaration:
placard = {'chemise': 3, 'pantalon': 6, 'tee-shirt': 7}
print(placard)

# Ne pas confondre avec un set:
mon_set = {'pseudo', 'mot de passe'}
print(mon_set)
# Un set ne prend que deux valeurs de même type.
# Supprimer des clés d'un dictionnaire:
# la fonction del (supprime, mais ne retourne rien)
del placard['chemise']
print(placard)
# La méthode pop (qui fait de même, mais retourne la valeur 
# comme si elle avait été extraite).
placard = {"chemise":3, "pantalon":6, "tee shirt":7}
print(placard)
extraction = placard.pop('chemise')
print(placard)
print(extraction)
placard = {"chemise":3, "pantalon":6, "tee shirt":7}
print(extraction)
extraction = placard.popitem()
print(extraction)
# extrait le premier élément du dico et retourne la
#  clé/valeur
# Comprehensions de dictionnaire
test = {x: x*x for x in (2, 4, 6)}
print(test)

# Parcourir les dictionnaires
chevaliers = {'gallahad': 'the pure', 'robin': 'the brave'}
# Parcourir les clés
for element in chevaliers:
  print(element)
# Reviens à
for cle in chevaliers.keys():
  print(cle)
# À l'inverse on peut ne parcourir que les valeurs:
for valeur in chevaliers.values():
  print(valeur)
# Parcourir les clés/valeurs (items)
for element in chevaliers.items():
  print(element)
# Parcourir pour afficher les clés puis les valeurs
for cle, valeur in chevaliers.items():
  print("Le chevalier {} dit {} ".format(cle, valeur))

# nombre d'items dans un dico fonction len()
print("Le nombre d'items dans le dico est: ", len(chevaliers))

# vérifier la présence d'une clé
test = 'gallahad' not in chevaliers
print(test)

# Stocker des fonctions dans un dico
def fete():
  print("C'est la fête")

def oiseau():
  print("Fais comme l'oiseau…")

fonctions = dict()
fonctions["fete"] = fete # on insert l'objet fonctino fete, mais on ne l'éxécute pas
# d'où l'absence des ()
fonctions["oiseau"] = oiseau
print(fonctions)
print(fonctions["oiseau"])
print(fonctions["oiseau"]())

# On peut stocker les références de fonctions dans n'importe quel
# conteneur: listes, dictionnaires et d'autres classes

# Refaire exercice fruits des listes, mais avec un dico.
####################
stockes = {
  'fraises': 76,
  'prunes':  51,
  'pommes':  22,
  'poires':  18,
  'melons':   4
}
# pour pouvoir ordonner, il faut passer en liste:
# en Une ligne
# stockes_trie = sorted([(fruit, nombre) for (nombre, fruit) in stockes.items()], reverse = True)
# En plus lisible,
# on transforme en liste de tuple
stockes_trie = [(fruit, nombre) for (nombre, fruit) in stockes.items()]
# On trie
stockes_trie = sorted(stockes_trie, reverse = True)
print(stockes_trie)

############################
#Les dictionnaires et paramètres de fonction
def fonction_inconnue(**parametres_nommes):
  """Fonction permettant de voir comment récupérer les 
  paramètres nommés dans un dico"""

  print("J'ai reçu en paramètres nommés: {}.".format(parametres_nommes))

fonction_inconnue()
fonction_inconnue(p=4, j=8) 
# Contraintes : cette façon de faire n'accepte que les paramètres nommés.
# Si l'on veut une fonction qui accepte n'importe quels paramètres :
# def fonction_inconnue(*en_liste, **en_dictionnaire)
# Ainsi tous les paramètres nommés se retrouveront dans la variable
# en_liste et les paramètres nommés dans en_dictionnaire.

# Transformer un dictoinnaire en paramètres nommés d'une fonction
parametres = {'sep': ' » ', 'end': ' -\n'}
print("Voici", "un", "exemple", "d'appel", **parametres)
# les paramètres nommés sont transmis à la fonction par un dictionnaire.

