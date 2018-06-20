
"""Experiment in progress…
"""
# Paramètre du nombre de coup avant que je joeur ne perde
count = 12

  # Liste des mots à trouver, proposés par le jeu.
game_list = [
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
  def generate_word_list_to_find(game_list) do
    game_list = 
    game_list
    |> Enum.random
    |> String.codepoints

    game_list_count = Enum.count(game_list)
    
    {game_list, game_list_count}
  end

  def word_user_init(game_list_count) do
    1..game_list_count
    |> Enum.map(fn n -> '*' end)
  end

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

  end
  defp check_one_char(nchar, user_char) when nchar == user_char, do: user_char
  defp check_one_char(nchar, user_char), do: '*'
end