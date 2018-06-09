import donnees
from fonctions import *

word_to_find_list, nb = generate_word_to_find(donnees.game_list)
print(word_to_find_list, ' ', nb)
searched_word_list = word_user_init(nb)
print(searched_word_list)
tries_int = 1
win_bool = False

while tries_int <= donnees.count and win_bool is False :
  user_char = getchar()
  searched_word_list = check_char(searched_word_list, word_to_find_list, user_char)
  if (word_to_find_list == searched_word_list) :
    print("Le mot est bien {}, en {} tetatives".format(searched_word_list, tries_int))
    print("RAF : Enregistrer le score")
    win_bool = True
  print("La liste est: {}, tentatives = {}".format(searched_word_list, tries_int))
  tries_int += 1

if win_bool :
  print("Gagné !")
  print("RAF : Votre Score est : $Score")
else:
  print("perdu !")

