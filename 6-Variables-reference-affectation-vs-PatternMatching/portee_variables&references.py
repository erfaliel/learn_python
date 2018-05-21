a = 5
def print_a():
    """Fonction chargée d'afficher la variable a.
    Cette variable a n'est pas passée en paramètre de la fonction.
    On suppose qu'elle a été créée en dehors de la fonction, on veut voir
    si elle est accessible depuis le corps de la fonction"""
    
    print("La variable a= {}.".format(a))

# Test de la fonction
print_a()
# on affecte une nouvelle valeur à a
a = 8
print_a()
# On conclu que la fonction ne trouvant pas a dans son espace locale
# est en capacité à remonté dans l'espace l'ayant appelé (donc en lecture)
