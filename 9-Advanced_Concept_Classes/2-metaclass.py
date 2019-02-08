#!/usr/bin/python3
# -*-coding:utf-8 -*
# We need to know that a class define an object, but class is an object to!
# __init__ special method allow to initiate new object, __new__ is a special method creating an object (before init)
# If __new__ return an instance, then __init__ is called
# __new__ is a static method (it doesn't use self, because object is not created yet)
# but it use "cls" that is the manipulated class;
class People:

  """ Class to define people.
  it owns attributs :
    -name
    -last_name
    -age
    -location
  name and last_name are forward to constructor."""

  def __new__(cls, name, last_name):
    print("Call to the method __new__ from the class : {}".format(cls))
    # Here Object will make the job
    return object.__new__(cls) # object build object from the class with 0 parameter
    # name and last will automatically passed to the consturctor

  def __init__(self, name, last_name):
    """ Our people constructor. """
    print("Call to the __init__ method")
    self.name = name
    self.last_name = last_name
    self.age = 23
    self.location = "New-York"

# exection
people = People("Manson", "Marylin")
print(people.last_name, " ", people.age)
"""Result :
Call to the method __new__ from the class : <class '__main__.People'>
Manson Marylin
Call to the __init__ method
Marylin   23"""

#Dynamic class
# As said before, Class is an object and accordingly depends on a class...
print(type(2)) # <class 'int'>
print(type(int)) # <class 'type'>
print(type("hello")) # <class 'str'>
print(type(str)) # <class 'type'>
# the "first class" is type
#type(name, tuple_class, dict )
#name : name of the class to buili
#tuple_class : classed to inherite into our new class
#dict: Dictionnary contains parameters and method names
# very basic case:
Person = type("Person", (), {})
print(Person)
print(type(Person))
""" Result :
<class '__main__.Person'>
<class 'type'>"""

#How to create method for a new metaclass
def person_create(person, name, last_name):
  """ A function which called to make the class Person constructor.
  parameters:
  -name
  -last_name"""
  person.name = name
  person.last_name = last_name
  person.age = 21
  person.location = "PARIS"

def person_print(person):
  """Fonction to print the person.
  Print only name and last name"""
  print("{} {}".format(person.last_name, person.name))

# Methods dictionnary
methods = {
  "__init__" : person_create,
  "print" : person_print,
}

# dynamically class creation
Person = type("Person", (), methods)

john = Person("Doe", "John")
print(john.name)
print(john.last_name)
print(john.age)
print()
john.print()

"""Resultat :
Doe
John
21

John Doe
"""
# Metaclass definition
# type is the default metaclass, but a class can get a metaclass other than type
# __new__ methods --> create class
# __init__ method --> buile class
class MyMetaClass(type):
  """Example for metaclass."""

  def __new__(metacls, name, bases, dict):
    """Metaclass creation."""
    print("We are creating our class: {}".format(name))
    return type.__new__(metacls, name, bases, dict)


class MyClass(metaclass=MyMetaClass):
  pass
### __init__ method uses same arguments than __new__ without the first (cls), name, mothers's classes tuple and
# dictionnary for attributs and methods of the class.

## Small example
# {
#   "Widget": Widget,
#   "Button": Button,
#   "RadioButton" : RadioButton,
#   "Menu": Menu,
#   "frame": Frame,
# }
track_classes = {} # Our empty dictionnary for now.
class MetaWidget(type):
  """Our metaclass for ours widgets.

  It inheritates from type, because it's first level metaclass.
  It will write into the track_classes dictionnary everytime a new class will be build with
  this metaclass."""

  def __init__(cls, name, bases, dict):
    """Metaclass constructor, called when a new class is created."""
    print("#ECHO: build a new class from MetaWidget: {}#".format(name))
    type.__init__(cls, name, bases, dict)
    track_classes[name] = cls

class Widget(metaclass=MetaWidget):

  """Mother class for our entire widgets."""
  pass

class Button(Widget):
  """A class for the button widget."""
  pass

class Menu(Widget):
  """A class for the menu widget."""
  pass

class RadioButton(Menu):
  """A subclass radiobutton."""
  pass


print("Track dictionnary : ", track_classes)

"""Result :
#ECHO: build a new class from MetaWidget: Widget#
#ECHO: build a new class from MetaWidget: Button#
#ECHO: build a new class from MetaWidget: Menu#
#ECHO: build a new class from MetaWidget: RadioButton#
Track dictionnary :  {'Button': <class '__main__.Button'>, 'Widget': <class '__main__.Widget'>, 'Menu': <class '__main__.Menu'>, 'RadioButton': <class '__main__.RadioButton'>}
"""
