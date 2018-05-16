# programme calculant années bisextiles
defmodule Annee do

  def is_bisextile?(annee) do
    cond do
      rem(annee, 4)   != 0 -> false
      rem(annee, 100) != 0 -> true
      rem(annee, 400) == 0 -> true
      true                 -> false
    end
  end
end

#main
annee = IO.gets "Entrez une année : "
annee = annee |> String.trim |> String.to_integer

case Annee.is_bisextile?(annee) do
  true  -> IO.puts "#{annee} est une année bisextile."
  false -> IO.puts "#{annee} n'est pas une année bisextile."
  _     -> IO.puts "Tu as encore du debug à faire mon gars…"
end