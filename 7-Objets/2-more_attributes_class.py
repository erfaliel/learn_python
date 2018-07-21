#!/usr/bin/python3
# -*-coding:utf-8 -*

class Person: # Def of our class Person
  """Class defining Person with attributes :
  - his last name
  - his first name
  - his age
  - his location where he lives """

  def __init__(self): # constructor : self is the actual object himself.
    """ Only a single attribute for the moment """
    self.name       = "Dupont"
    self.first_name = "Bernard"
    self.age        = 42
    self.location   = "CAEN"

bernard = Person() # Create a new Person type var (always execute __init__ constructor methode)
print("Create instance of object: bernard = Person() -> {} ".format(bernard))
print("bernard.name : {}".format(bernard.name))
print("bernard.first_name : {} ".format(bernard.first_name))
print("bernard.location : {} ".format(bernard.location))
bernard.location = "PARIS"
print("new assigned location: bernard.location = 'PARIS' -> {} ".format(bernard.location))