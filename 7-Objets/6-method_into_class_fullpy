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
  def erase(self):
    """ erase alows to delete message by forcing message to "" """
    self.surface = ""
  def print(self):
    """ print alows to… print """
    print(self.surface)

# Test 

dash = DashBoard()
dash.write("I'm writing on the dashboard")
dash.print()
dash.write("I'm writing again !")
dash.print()
dash.erase()
dash.print()
