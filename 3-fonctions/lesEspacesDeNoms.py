# changement de l'espace de nom math vers mathematiques
import math as mathematiques
π = mathematiques.pi
print("π = ", π)

# ne récupérer qu'une fonction du module et l'utiliser dans 
# l'espce de nom courant.
from math import sqrt
# from math import * # est également possible.
sqrt(4)
