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
    for cle, valeur in self.items(): # implique de definir self.items()
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

