# -*-coding:utf-8 -*
def table(nb, max=10): #max à une valeur par défaut si elle n'est pas appelée.
  # On commence par le docstring pour avoir help(table)
  """Fonction affichant la table de multiplication par nb
  de 1*nb à max*nb

  (max >= 0)
  
  Appelle de la fonction par : maPremiereFonction.table(a, [b])"""
  i = 0
  while i < max:
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1

def fonction_nommee(a=1, b=2, c=3, d=4, e=5):
  """Essayer en ne rentrant aucun paramètres, puis
  quelques paramètres dans l'ordre de votre choix """
  print("a =", a, "b =", b, "c =", c, "d =", d, "e =", e)

def renvoyer_carre(valeur):
  """Généralement une fonction renvoie une valeur que l'on pourra
  stocer dans une variable.
  Essayer par exemple valeur = renvoyer_carre(5)"""
  return valeur * valeur