#!/usr/bin/python3
# -*-coding:utf-8 -*

class DashBoard:
  """ Place where you can write, read our erase with method.
  Modified attribut is 'surface'. """

  def __init__(self):
    """ By default, surface is empty. """
    self.surface = ""
  def write(self, message):
    """ Method to write on dashboard surface.
    if surface is not empty, we pass to next line before to
    write the message. """

    if self.surface != "":
      self.surface += "\n"
    self.surface += message

# Test 

dash = DashBoard()
dash.write("Test du tableau !")
dash.surface
print(dash.surface)
dash.write("Il fonctionne bien")
print(dash.surface)
print("les attributs (self) sont contenu dans l'objet.")
dash_b = DashBoard()
dash_b.write("En créant un autre objet dash_b = DashBoard() \
->J'écris sur un autre tableau")
print(dash_b.surface)
print("Les méthodes appartiennent à la classe.")
print("dash : {}, \ndash_b : {}. ".format(dash.write, dash_b.write))
print("DashBoard.write is just a function : {}. ".format(DashBoard.write))
print("We can consult the help of the method help(DashBoard.write): {}. ".format(help(DashBoard.write)))
print("If we streadfully call the method of the class, it  works, DashBoard.write(dash, 'check')") # self is the object dash here
DashBoard.write(dash, "check")
print(dash.surface)
