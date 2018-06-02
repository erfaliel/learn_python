import random
import re

def generate_word_to_find(game_list):
  """Take a list and return a tuple.
  from a list, extract a word by random fonction, change this word into a list and the number of
  the char for this one."""

  word_to_find_char = random.choice(game_list)
  number_word_to_find_int = len(word_to_find_char)
  word_to_find_list = [char for char in word_to_find_char]
  return (word_to_find_list, number_word_to_find_int)

def getchar():
  """ return a char entered by the user if it is one char only. """
  char = ''
  while re.match(r"^[a-zA-Z]$", char) is None :
    char = input("Entrez un caractère et un seul : ")
  return char

def check_char(searched_word_list, word_to_find_list, user_char):
  """Take two list and a char and return the modified first list.
  the fonction allowed to check if user_char is in word_to_find_list.
  So it sets the char in the correct slot of the searched_word_list. """

  for (index, element) in enumerate(word_to_find_list):
    if element == user_char :
      searched_word_list[index] = user_char
  return searched_word_list

def word_user_init(number_word_to_find_int):
  """Take an integer and return a list.
  form integer, generate a list of '*'. """ 

  searched_word_list = list()
  i = 0
  while i < number_word_to_find_int :
    searched_word_list.append('*')
    i += 1
  return searched_word_list

# Unit tests 
if __name__ == "__main__" :
  game_list = ['toto', 'otot']
  (word_to_find_list, number_word_to_find_int) = generate_word_to_find(game_list)
  print(word_to_find_list)
  print(number_word_to_find_int)
  searched_word_list = word_user_init(number_word_to_find_int)
  print(searched_word_list)
  print(check_char(searched_word_list, word_to_find_list, 'o'))
