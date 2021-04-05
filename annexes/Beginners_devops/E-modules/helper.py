status = -1
message_user= "Saisir le nombre de jour et l'unité de conversion: \n"

def convert_days(user_input):
    """(dict{string, string}) -> tuple(string, integer)
    convert user input to number of hours.
    output : 
        string  : message output
        integer : status"""
    print(user_input)
    number_of_days = user_input["days"]
    unit= user_input["unit"]
    try:
        number_of_days= int(number_of_days)
        # We only want convert positive integers.
        if number_of_days > 0:
            return days_to_units(number_of_days, unit)
        if number_of_days == 0:
            return ("Entrez un nombre supérieur à zéro.", 1)
        if number_of_days < 0:
            return (f"{number_of_days} is a negative number: try again !", 2)
    except ValueError:
        return (f"\"{number_of_days.strip()}\" is not au number. ", 3)

def days_to_units(number_of_days, unit):
    some = "s font" if number_of_days > 1 else " fait" # ternary in Python
    if unit == "hours":
        return (f"{number_of_days} jour{some} {number_of_days * 24} heures", 0)   
    elif unit == "minutes":
        return ( f"{number_of_days} jour{some} {number_of_days * 24 * 60} minutes", 0 )
    else:
        return ("unsuported unit", -1 )
