import os #utiliser pour les fonctions os

print(os.getcwd()) # répertoire courant.
print('On change de répertoire…')
os.chdir("fichiers_dir") #Se rendre dans le répertoire (ici relatif)
print(os.getcwd()) # vérifier que l'on a bien changé de répertoire. 

#Lire un fichier
# r: lecture, w: écriture (efface le contenu précédent, crée le fichier s'il n'existe pas).
# a: append (écrit à la fin du fichier existant). b: mode binaire.
mon_fichier = open("fichier_py.txt", "r")
print(mon_fichier)
print("type de mon_fichier", type(mon_fichier))

