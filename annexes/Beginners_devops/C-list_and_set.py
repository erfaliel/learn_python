name_of_units = "hours"
calculation_to_unit = 24
status = -1

def checkInputUser(user_input):
    """(string) -> set (string, integer)
    convert user input to number of hours.
    output : 
        string  : message output
        integer : status"""

    try:
        user_input = int(user_input)
        # We only want convert positive integers.
        if user_input > 0:
            return (f"{user_input} days are {int(user_input) * calculation_to_unit} {name_of_units}", 0)
        if user_input == 0:
            return ("Entrez un nombre supérieur à zéro.", 1)
        if user_input < 0:
            return (f"{user_input} is a negative number: try again !", 2)
    except ValueError:
        return (f"\"{user_input.strip()}\" is not au number. ", 3)


user_input = input("Saisir la valeur à convertir: \n")
# num_of_days = set(user_input.split(", "))
num_of_days = user_input.split(", ")
num_of_days = set(num_of_days) # set type conversion to supress doublon
print(type(num_of_days))
print(num_of_days)
for num_of_days_element in num_of_days:
    (value, status) = checkInputUser(num_of_days_element)
    print(f"( {value}, status: {status} )")

