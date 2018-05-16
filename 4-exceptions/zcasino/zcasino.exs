defmodule Zcasino do
  def get_number do
    number = IO.gets "Saisissez un nombre entre 0 et 49 : "
    cond do
      number =~ ~r{^[0-9]*[0-9]$} -> 
        number = number |> String.trim |> String.to_integer
        check_number {:ok, number}
      true                        ->
        check_number {:err, "is_not_a_number"}
    end
  end

  defp check_number({:err, _})  do
    IO.puts "Vous devez entrer un nombre !"
    get_number()
  end
  defp check_number({:ok, number}) when number < 0 do
    IO.puts "Le nombre ne peut être négatif !"
    get_number()
  end
  defp check_number({:ok, number}) when number > 49 do
    IO.puts "Le nombre ne peut être supérieur à 49 !"
    get_number()
  end
  defp check_number(value), do: value
end
    
# Main
Zcasino.get_number()
|> Zcasino.get_mise()

