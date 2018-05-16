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