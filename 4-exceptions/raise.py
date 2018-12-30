annee = input("Saisir une année : ") # L'utilisateur saisit l'année
try:
    annee = int(annee) # On tente de convertir l'année
    if annee<=0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")

# À noter que le bloc try: except est factultatif mais montre
# que le raise peut être catchée.
# assert «test» se distingure de if «test» raise que dans le premier
# cas on obtient une AssertionErron et dans le second on indique le
# type de l'exception.S
# Ci dessous les built-in exceptions:
# https://docs.python.org/fr/3/library/exceptions.html
