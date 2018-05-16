# -*-coding:utf-8 -*

import os
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
# Test unitaire de la fonction table
# --Cette partie ne sera pas utilisée à l'import--
# --Mais uniquement à l'exécution direct de se programme.--
if __name__ == "__main__":
  table(4)
  os.system("pause")