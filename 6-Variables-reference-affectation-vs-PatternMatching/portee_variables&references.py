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

# Variables dans un corps de fonction
def set_var(nouvelle_valeur):
    """Fonction nous permettant de tester la portée des variables
    défifinies dans notre corps de fonction"""

    # On essaye d'afficher la variable var, si elle existe
    try:
        print("Avant l'affectation, notre variable var vaut {0}. ".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    var = nouvelle_valeur
    print("Après affectation, notre variable var vaut {0}. ".format(var))

set_var(5)
# var #Si décommenté, on voit que l'affectation de var n'existe plus au delà de la fonction.

# Une fonction modifiant les objets
def ajouter(liste, valeur_a_ajouter):
    """Cette fonction insère à la fin de la liste la valeur que l'on veut
    ajouter"""
    liste.append(valeur_a_ajouter)

ma_liste = ['a', 'e', 'i']
ajouter(ma_liste, 'o')
print(ma_liste)
# avec cette fonction cette fois même au sortir de la fonction la variable est conservé.
# Mais c'est différents car on utilise une méthode de l'objet pour le modifier.

# Copie vs Référence
ma_liste1 = [1, 2, 3]
ma_liste2 = ma_liste1 # ici on passe la référence et non la valeur de l'objet
ma_liste2.append(4)
print(ma_liste2)
print(ma_liste1) 

# Par contre les flottants, les entiers, les chaînes de caractères n'ont pas de méthode modifiant 
# l'objet lui même, mais en retourne un nouveau, donc dans ce cas on obtient une copie avec sa propre référence.
# Forcer la copie d'objet plutôt que d'avoir la même référence.
ma_liste1 = [1, 2, 3]
ma_liste2 = list(ma_liste1) # On utilise le constructeur de l'objet liste: Je crée un objet liste et j'indique 
# le contenu à y mettre
ma_liste2.append(4)
print(ma_liste2)
print(ma_liste1) 
# pour rappel pour un dictionnaire,nous aurions utilisé le constructeur dict().

# Variables globales
i = 4
def inc_i():
    """Fonction chargée d'incrémenter i de 1"""
    global i # Python recherche i en dehors de l'espace local de la fonction
    i += 1

print(i)
inc_i()
print(i)
