import donnees
from fonctions import *

#Get randomly a word in the list
word_to_find_list, nb = generate_word_to_find(donnees.game_list)
#debug# print(word_to_find_list, ' ', nb)
# Generate word to find with *
searched_word_list = word_user_init(nb)
print("voici un mot en {} lettres à trouver :".format(nb))
print(searched_word_list)
# Init games
tries_int = 1
win_bool = False
scores_dict = get_scores() #get existing scores in file
# get the name of the current player
player_name_string = input("Veuillez saisir votre nom : ")
# check player or create player score
player_name_string, score_player_int = get_score_player(scores_dict, player_name_string)
print("Bonjour {}, ton score actuel est de {}.".format(player_name_string, score_player_int))

while tries_int <= donnees.count and win_bool is False :
  user_char = getchar()
  searched_word_list = check_char(searched_word_list, word_to_find_list, user_char)
  if (word_to_find_list == searched_word_list) :
    print("Le mot est bien {}, en {} tetatives".format(searched_word_list, tries_int))
    win_bool = True
  print("La liste est: {}, tentatives = {}".format(searched_word_list, tries_int))
  tries_int += 1

if win_bool :
  print("Gagné !")
  score_int = donnees.count - tries_int
  print("Votre score pour cette partie est : {}.".format(score_int))
  # Calculate new score for the player
  (player_name_string, score_player_int) = calculate_score_player((player_name_string, score_player_int), score_int)
  print("Votre nouveau score au jeu est : {}".format(score_player_int))
  # Enregistrement du nouveau score
  scores_dict[player_name_string] = score_player_int
  save_scores(scores_dict)
else:
  print("perdu ! Le mot à trouver était : {}".format(word_to_find_list))
  print("Votre score est inchangé, il est de : {}".format(''.join(score_player_int)))