#!/usr/bin/python3
# -*-coding:utf-8 -*

class Person: # Def of our class Person
  """Class defining Person with attributes :
  - his last name
  - his first name
  - his age
  - his location where he lives """

  def __init__(self, name, first_name): # constructor : self is the actual object himself and 2 attributes to init.
    """ Only a single attribute for the moment """
    self.name       = name        # Affect an attribute via the var passed by the constructor.
    self.first_name = first_name
    self.age        = 42
    self.location   = "CAEN"

bernard = Person("GARCIA", "Vincent") # Create a new Person type var (always execute __init__ constructor methode)
                                      # Self is not used (it is implicit) during the object creation only into the class.
print("Create instance of object: bernard = Person() -> {} ".format(bernard))
print("bernard.name : {}".format(bernard.name))
print("bernard.first_name : {} ".format(bernard.first_name))
print("bernard.location : {} ".format(bernard.location))
bernard.location = "PARIS" # Attribute modification
print("new assigned location: bernard.location = 'PARIS' -> {} ".format(bernard.location))
# New object
new_person = Person("MANSON", "Marylin")
print("Create instance of object: new_person = Person() -> {} ".format(bernard))
print("new_person.name : {}".format(new_person.name))
print("new_person.first_name : {} ".format(new_person.first_name))
print("new_person.location : {} ".format(new_person.location))

print("So attributes are bound to the object !")