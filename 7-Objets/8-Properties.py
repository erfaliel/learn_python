#!/usr/bin/python3
# -*-coding:utf-8 -*

class Person: # Def of our class Person
  """Class defining Person with attributes :
  - his last name
  - his first name
  - his age
  - his location where he lives """

  def __init__(self, name, first_name): # constructor : self is the actual object himself.
    """ Only a single attribute for the moment """
    self.name       = name
    self.first_name = first_name
    self.age        = 42
    self._location   = "CAEN"
  def _get_location(self):
    """ Method to access attribut _location on read only """
    print("we get location attribut")
    return self._location
  def _set_location(self, new_location):
    """ Method to set attribut _location """
    print('Be carefull, it seems than {}, relocate to {}. '.format(
        self.first_name, new_location
    ))
    self._location = new_location

  # We have to declare to Python that _location attribut is a property
  location = property(_get_location, _set_location)

  # Sum up 
  # nom_propriete = property(methode_accesseur, methode_mutateur, methode_suppression, methode_aide)
  
bernard = Person("Dupont", "Bernard") # Create a new Person type var (always execute __init__ constructor methode)
print("Create instance of object: bernard = Person() -> {} ".format(bernard))
print("bernard.name : {}".format(bernard.name))
print("bernard.age: {}".format(bernard.age))
print("bernard.first_name : {} ".format(bernard.first_name))
print("bernard.location : {} ".format(bernard.location))
bernard.location = "PARIS"
print("new assigned location: bernard.location = 'PARIS' -> {} ".format(bernard.location))
