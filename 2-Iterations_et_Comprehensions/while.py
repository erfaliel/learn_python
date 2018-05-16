# Boucle While (Itération dans Python)
i = 1
while i < 20:           # Tant que il est inférieur à 20
  if i % 3 == 0:        # Si i est un multiple de 3
    i += 4              # on incrémente 4
    print("on incréemente i de 4. i est mainteant égale à ", i)
    continue            # On retourne au while directemnt
  print("La variable i = ", i)
  i += 1                # inclément classique de while

  #À l'inverse du mot-clé «continue», il existe le mot-clé «break»
