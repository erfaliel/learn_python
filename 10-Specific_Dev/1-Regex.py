import re # regexp module

# To prevent escape character you can use r'' : \\n <=> r'\n'
"""
on vérifie caractère / caractère sauf s'il s'agit d'un groupe.
(abc) : groupe de caractère ce qui signifie : a suivi de b suivi de c
^ : commence obligatoirement par.
$ : Termine obligatoirement après cd qui précède.
* : se répète 0, 1 ou plus abc*  --> 'ab', 'abc', 'abcc', 'abcccccc'
+ : au moins 1 ou plus occurences.
? : 0 ou 1 occurence (ce qui correspond à une séquence optionnelle)
{n} : nombre précis d'occurence ou n est le nombre d'occurence.
    {2, 4} de 2 à 4 fois
    {, 5} de 0 à 5 fois
    {6,} de 8 fois minimum
[abc] : Classe de caractère ce qui signifie l'un des caractère (a ou b ou c)"""



print(r'\n') # r''  doesn't need to escape with r'' otherwise you need to type '\\n'
print(re.search(r'abc', "abcdef"))
print(re.search(r"abs", "absolue"))
print(re.search(r"abs", "tabsolue"))

print(re.search(r'(cha){2}', "chacha"))
print(re.search(r'(cha){2}', "chachachat"))
print(re.search(r'(cha){2}', "chachichit")) #KO

print(re.search(r'^0[0-9][ .-]([0-9]){2}', "01-02"))
print(re.search(r'^0[0-9][ .-]([0-9]){2}', "01-02-03"))
print(re.search(r'^0[0-9][ .-]([0-9]){2}', "01_02-03")) #KO
print(re.search(r'^0[0-9]([ .-]([0-9]){2}){4}', "01-02-03-04-05"))
print(re.search(r'^0[0-9]([ .-]([0-9]){2}){4}', "06-60-03-14-75"))
print(re.search(r'^0[0-9]([ .-]?([0-9]){2}){4}', "06-60-03-14-75")) 
print(re.search(r'^0[0-9]([ .-]?([0-9]){2}){4}', "0660031475")) # Le ? rend optionnel le délimiteur.
print(re.search(r'^0[0-9]([ .-]?([0-9]){2}){4}$', "06 60 03 14 75")) #$ impose la fin
print(re.search(r'^0[0-9]([ .-]?([0-9]){2}){4}$', "06 60 03 14 75 38")) # KO

# Usefull with condition : re.match that return a boolean
expression = r'^[1-5][A-Za-z]*.$' # start with number from 1 to 5, followei by char (we don't know how many), but must ended by a "."
chaine ="3qfAFxeA."
if re.match(expression, chaine) is not None:
    print("Weldone!")

# More consise 
if re.match(expression, chaine):
    print("Weldone!!!")

# How to replace an expression : re.sub
# what to search, what to replace with, chain
test = re.sub(r'pi', r'π', "apitoka")
print(test) # aπtoka
# we are be able to use group with group number
# with (ab)c(def) \1 is the group number for (ab) (not 0 ?) and (def) is \2
test = re.sub(r'(ab)', r'[  \1 ]', "yzabcdef")
print(test) #  yz[  ab ]cdef

# we can use name group instead of group number
# to name a group, you have to ( : open group, add "?P" characters, put name between "<>" character
# to call this group by its name : \g followed by name between "<>" character
match = r'id=(?P<id>[0-9]+)'
replace = r'id[\g<id>]'

print(re.sub(match, replace, "id=128"))
print(re.sub(match, replace, "id=128Y34"))

# Compiled regexp to create a reusable regexp object
# When you often need to use a regexp in your program, you can compile the regexp in an object:
# It is helpfull, and more effective for performance 
valid_pwd_chain = r'^[A-Za-z0-9]{6,}$' # regexp
exp_pwd_object = re.compile(valid_pwd_chain) # compile in object
pwd = ""
while not exp_pwd_object.match(pwd): # or while exp_pwd_object.search(pwd) is None:
    pwd = input("create  your password : ")
