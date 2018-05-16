#main
annee = IO.gets "Entrez une année : "
annee = annee |> String.trim |> String.to_integer

if rem(annee, 400) == 0 or (rem(annee, 4) == 0 and rem(annee, 100) != 0) do
  IO.puts "#{annee} est une année bisextile."
else
  IO.puts "#{annee} n'est pas une année bisextile."
end