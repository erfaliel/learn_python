#!/usr/bin/python3
# -*-coding:utf-8 -*

class DictionnaireOrdonne:
  """ Notre dictionnaire ordonné. L'ordre des données est maintenu
  et il peut donc, contrairement aux dictionnaires usuels, être trié
  ou voir l'ordre de ses données inversées"""

  def __init__(self, base={}, **donnees):

    self._cles = [] # Liste contenant nos clés ce qui permettra d'ordonner
    self._valeurs = [] # Liste contenant nos valeurs

    # On vérifie que 'base' est un dictionnaire exploitable
    if type(base) not in (dict, DictionnaireOrdonne):
      raise TypeError("le type attendu est un dictionnaire (usuel ou ordonne)")
    # On récupère les données dans 'base'
    for cle in base:
      self[cle] = base[cle] # cette affectation implique d'écrire __setitem__
    # On récupère les données dans 'donnees'
    for cle in donnees:
      self[cle] = donnees[cle] # cette affectation implique d'écrire __setitem__

  def __setitem__(self, cle, valeur):
    """Méthode spéciale appelée quand on cherche à modifier une clé
    présente dans le dictionnaire. Si la clé n'est pas présente, on l'ajoute
    à la fin du dictionnaire"""

    if cle in self._cles:
      curseur = self._cles.index(cle)
      self._valeurs[curseur] = valeur
    else:
      self._cles.append(cle)
      self._valeurs.append(valeur)

  def __repr__(self):
    """Représentation de notre objet. C'est cette chaîne qui sera affichée
    quand on saisit directement le dictionnaire dans l'interpréteur, ou en
    utilisant la fonction 'repr'"""

    chaine = "{"
    premiere_boucle = True
    for cle, valeur in self.items(): # implique de definir le générateur self.items()
      if not premiere_boucle:
        chaine += ", "
      else:
        premiere_boucle = False
      chaine += repr(cle) + ": " + repr(valeur)
    chaine += "}"
    return chaine
  
  def items(self):
    """Renvoie un générateur contenant les couples (cle, valeur)"""

    for i, cle in enumerate(self._cles):
      valeur = self._valeurs[i]
      yield (cle, valeur)

  def __delitem__(self, cle):
    """Supprime la clé et la valeur associée dans l'objet"""

    if cle not in self._cles:
      raise KeyError("La cle {0} n'est pas présente dans l'objet".format(cle))
    else:
      curseur = self._cles.index(cle)
      del(self._cles[curseur])
      del(self._valeurs[curseur])

  def len(self):
    """Renvoie le nombre d'items contenu dans l'objet"""
    return len(self._cles)

  def __iter__(self):
    """ Retourne l'itérateur pour parcourir: ici on utilise l'itéteur de liste di self._cles"""
    return iter(self._valeurs)

  def keys(self):
    """ Retourne la liste des clé """
    return list(self._cles)

  def values(self):
    """Retourne la liste des valeurs """
    return list(self._valeurs)

  def sort(self):
    """Reclasse les items de la liste dans l'ordre des valeurs """
    # On définit deux liste temporaires pour travailler sur les items
    # On commence par trier les clés
    cles_triees = sorted(self._cles)
    # On génère la nouvelle liste des valeurs dans l'ordre de la liste cles
    valeurs = []
    for cle in cles_triees:
      valeur = self[cle]   # nécessite __getitem__ sinon "TypeError: 'DictionnaireOrdonne' object is not subscriptable"
      valeurs.append(valeur)
    
    # On mets à jour les éléments de l'objets
    self._cles = cles_triees
    self._valeurs = valeurs



    


fruits = DictionnaireOrdonne()
fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15
print(fruits)
# print(fruits["pomme"])
# print(fruits["melon"])
# print(fruits)
vegetables = DictionnaireOrdonne(carotte = 26, haricot = 48, poire = 270)
print(vegetables)
vegetables["fraise"] = 18
print(vegetables)
vegetables["poire"] = 27
print(vegetables) 
print("nombre d'éléments dans vegetables: {}".format(vegetables.len()))
del(vegetables["carotte"])
print("nombre d'éléments dans vegetables: {}".format(vegetables.len()))
# del(vegetables["carotte"])
print(vegetables["poire"])
print("liste des clés de vegetables: {}".format(vegetables.keys()))
print("liste des valeurs de 'vegetables': {}".format(vegetables.values()))
print("sorted 'vegetables': {}".format(vegetables.sort()))