#!/usr/bin/python3
# -*-coding:utf-8 -*
# Basic Class
class Person: # Def of our class Person
  """Class defining Person with attributes :
  - his last name
  - his first name
  - his age
  - his location where he lives """

  def __init__(self): # constructor : self is the actual object himself.
    """ Only a single attribute for the moment """
    self.name = "Dupont"

bernard = Person() # Create a new Person type var (always execute __init__ constructor methode)
print("Create instance of object: bernard = Person() -> {} ".format(bernard))
print("bernard.name : {}".format(bernard.name))