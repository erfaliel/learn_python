annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0   # Il s'agit un test qui a pour résultat de lever une erreur si le test échoue
# L'assertion peut être «catchée» par except.
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
