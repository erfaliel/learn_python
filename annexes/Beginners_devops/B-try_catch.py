name_of_units = "hours"
calculation_to_unit = 24
status = -1

def checkInputUser(user_input):
    try:
        user_input = int(user_input)
        if user_input > 0:
            return (f"{user_input} days are {int(user_input) * calculation_to_unit} {name_of_units}", 0)
        if user_input == 0:
            return ("Entrez un nombre supérieur à zéro.", 1)
        if user_input < 0:
            return (f"{user_input} is a negative number: try again !", 2)
    except ValueError:
        return (f"{user_input} is not au number. ", 3)

while status != 0:
    user_input = input("Saisir la valeur à convertir: \n")
    (value, status) = checkInputUser(user_input)
    print(f"( {value}, status: {status} )")

