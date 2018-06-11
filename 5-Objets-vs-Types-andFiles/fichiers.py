import os #utiliser pour les fonctions os

print(os.getcwd()) # répertoire courant.
print('On change de répertoire…')
os.chdir("fichiers_dir") #Se rendre dans le répertoire (ici relatif)
print(os.getcwd()) # vérifier que l'on a bien changé de répertoire. 

#Utiliser un fichier##################################
# r: lecture, w: écriture (efface le contenu précédent, crée le fichier s'il n'existe pas).
# a: append (écrit à la fin du fichier existant). b: mode binaire.
mon_fichier = open("fichier_py.txt", "r")
print(mon_fichier)
print("type de mon_fichier", type(mon_fichier))
mon_fichier.close() #Toujour prendre l'habitude de fermer pour ne pas locker

# Ainsi quand on sort du bloque, alors le fichier est femé (même en cas de plantage)

#Lire l'intégralité d'un fichier
mon_fichier = open("fichier_py.txt", "r")
contenu = mon_fichier.read()
print("lecture du contenu du fichier")
print(contenu)
mon_fichier.close()
# contenu est un objet de type chaine avec toutes les méthodes qui vont avec.

# Sécurisation de l'accès au fichier avec with (permet que le fichier se ferme en auto.)
with open("fichier_py.txt", "r") as mon_fichier:
    contenu = mon_fichier.read()
    print("Lecture du contenu du fichier en mode «with»")
    print(contenu)
# Écrire dans un fichier
with open("fichier.txt", 'a') as mon_fichier:
    nb_char_insterted = mon_fichier.write("Je rajoute cette ligne à mon fichier via python. /n")
    print("J'ai écris {} caractères".format(nb_char_insterted))
# la méthode write prend en entrée que des chaînes de caractères.
# Elle retourne le nombre de caractères insérés dans le fichier.
# Si pour mémoriser des nombres (ex: score), il faudra au préalable
# faire une conversion en chaine de caractères.


# Je relis mon fichier
with open("fichier_py.txt", "r") as mon_fichier:
    contenu = mon_fichier.read()
    print("Lecture du contenu du fichier en mode «with»")
    print(contenu)
# le module os a plein de méthode pour travailler sur le fichiers.
# variable de l'environnement
os.environ
os.name()
# os.chown(fd, uid, gid)

# Enregistrer des objets dans des fichiers
# nous allons utiliser le module pickle.
# on peut enregistrer un objet par fichier ou les mettre les uns à la suite des autres dans un seul.
import pickle
score = {
    'joueur 1' :  5,
    'joueur 2' : 35,
    'joueur 3' : 20,
    'joueur 4' :  2
}
# Enregistrement de l'objet:
with open('donnees', 'wb') as fichier_contenant_objet:
    mon_pickler = pickle.Pickler(fichier_contenant_objet)
    mon_pickler.dump(score)

# Récupérer l'objet dans le fichier
# Unpickler
with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load() # cela renvoit le premier objet du fichier.
    # Si nécessaire appeler autant de fois que d'objet.
print("Le score récupéré est : {}".format(score_recupere))

