import helper as h  # as is optiona, but you need to call helper.conver_days

user_input = input("Saisir le nombre de jour et l'unité de conversion: \n")
# num_of_days = set(user_input.split(", "))
days_and_unit = user_input.split(":")
print(type(days_and_unit))
print(days_and_unit)
days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
print(type(days_and_unit_dictionary))
print(days_and_unit_dictionary)
print(h.convert_days(days_and_unit_dictionary))