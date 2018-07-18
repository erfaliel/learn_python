
"""Experiment in progress…
"""
# Paramètre du nombre de coup avant que je joeur ne perde
count = 12

  # Liste des mots à trouver, proposés par le jeu.
game_words_list = [
  "nez",
  "jet",
  "jeu",
  "zoo",
  "fer",
  "dos",
  "riz",
  "tir",
  "emu",
  "abus",
  "ados",
  "banc",
  "bile",
  "brut",
  "brai",
  "chat",
  "demo",
  "deco",
  "dodu",
  "aimer",
  "verge",
  "video",
  "vitre",
  "abusif",
  ]
IO.inspect game_list
IO.inspect count
defmodule Pendu do
  def generate_word_to_find(game_words_list) do
    game_word_string = Enum.random(game_words_list)
    game_word_count_int = Enum.count(game_list)
    
    {game_word_string, game_word_count_int}
  end

  def found_letters(found_letters_list, game_word_string) do
    String.codepoints game_word_string
    |> Enum.map(fn n -> check_char(found_letters_list, n) end)
    |> to_string
  end

  def check_char(found_letters_list, nchar) do
    found_letters_list
    |> Enum.map(&(check_one_char(&1, nchar)))
  end

  def check_one_char(n, nchar) when n == nchar, do: nchar
  def check_one_char(n, nchar), do: "*"

  def get_char do
    user_char = IO.gets("Veuillez entrer un caractère et un seul : ")
    |> String.trim_trailing
    |> String.downcase
    
    cond do
      Regex.match?(~r{^[a-zA-Z]$}, user_char) -> user_char
      true                               -> get_char()
    end
  end

  def check_char(searched_word_list, word_to_find_list, user_char) do
    word_to_find_list
    |> Enum.map(fn nchar -> check_one_char(nchar, user_char) end)
    |> Enum.map(fn nchar ->)

  end

end