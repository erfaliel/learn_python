from helper import convert_days, message_user #more specific way

user_input = input(message_user)
# num_of_days = set(user_input.split(", "))
days_and_unit = user_input.split(":")
print(type(days_and_unit))
print(days_and_unit)
days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
print(type(days_and_unit_dictionary))
print(days_and_unit_dictionary)
print(convert_days(days_and_unit_dictionary))