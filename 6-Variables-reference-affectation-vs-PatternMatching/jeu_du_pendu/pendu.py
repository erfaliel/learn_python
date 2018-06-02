import donnees
from fonctions import *

word_to_find_list, nb = generate_word_to_find(donnees.game_list)
print(word_to_find_list, ' ', nb)
searched_word_list = word_user_init(nb)
print(searched_word_list)
tries = 1
while tries <= donnees.count :
  user_char = getchar()
  searched_word_list = check_char(searched_word_list, word_to_find_list, user_char)
  if (word_to_find_list == searched_word_list) :
    print("Le mot est bien {}, en {} tetatives".format(searched_word_list, tries))
    print("Enregistrer le score")
  print("La liste est: {}, tentatives = {}".format(searched_word_list, tries))
  tries += 1

print("perdu !")

