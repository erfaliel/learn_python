#!/usr/bin/python3
# -*-coding:utf-8 -*

class Test:
  """ a class for the need of our test """
  def __init__(self):
    """ Just one attribut for the constructor """
    self.my_attribut = "ok"
  
  def print_attribut(self):
    """ Method to print my attribut """
    print("My attribut is {}.".format(self.my_attribut))

my_test = Test()          # create new object
my_test.print_attribut()  # execute the methode of this object

print(dir(my_test))       # print properties of the object
print("my__test__.dict vaut :", my_test.__dict__) # we can select which propertie to print
my_test.__dict__["my_attribut"] = 'Not ok anymore.' # we can change attribut like that to (but this internal procedure is not for the dev)
my_test.print_attribut()  # is the attribut change works ? yes !

