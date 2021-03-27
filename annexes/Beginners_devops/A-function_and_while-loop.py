name_of_units = "hours"
calculation_to_unit = 24
status = -1

def checkInputUser(user_input):
    if user_input.isdigit():
        user_input = int(user_input)
        (value, status) = days_to_units(user_input)
        return (value, status)
    else:
        return (f"{user_input} is not au number. ", 3)

def days_to_units(num_of_days):
    if num_of_days > 0:
        return (f"{num_of_days} days are {int(num_of_days) * calculation_to_unit} {name_of_units}", 0)
    if num_of_days == 0:
        return ("Entrez un nombre supérieur à zéro.", 1)
 

while status != 0:
    user_input = input("Saisir la valeur à convertir: \n")
    (value, status) = checkInputUser(user_input)
    print(value)

