#!/usr/bin/python3
# -*-coding:utf-8 -*
class A:
  """ Class A, to make a simple exemple"""
  pass # to nothing

class B(A):
  """ This class B, that inherit from class A:
  You get the same attributes and methods than A."""

  pass

# First Python get methods from class B, else get up from class A.

class Person:
  """Class to mean a person """
  def __init__(self, name):
    """Person class Constructor"""
    self.name = name
    self.lastname = "Marylin"
  def __str__(self):
    """Method called when object is converted in string"""
    return "{0} {1}".format(self.lastname, self.name)

class SpecialAgent(Person):
  """Class meaning special agent.
  It inherits from Person class."""
  def __init__(self, name, serial_number):
    """ An agent is defined by his name and matricul"""
    self.name = name
    self.serial_number = serial_number
  def __str__(self):
    """Method called when object ist converted in string"""
    return "Agent {0}, Serial Number {1}".format(self.name, self.serial_number)

agent = SpecialAgent("Fisher", "1837-121")
print(agent.name)
print(agent)
#print(agent.lastname) : You cannot do this, because Construtor of SpecialAgent overide its mother class Person
#But Remember : My_object.my_method() equal MyClass.My_method(My_object), so here My_object is self. 

class SpecialAgentα(Person):
  """Class meaning special agent.
  It inherits from Person class."""
  def __init__(self, name, serial_number):
    """ An agent is defined by his name and matricul"""
    Person.__init__(self, name) # overide mother constructor with same values
    self.serial_number = serial_number # and Add new value. 
  def __str__(self):
    """Method called when object ist converted in string"""
    return "Agent {0}, Serial Number {1}".format(self.name, self.serial_number)

agent = SpecialAgentα("Fisher", "1837-121")
print(agent.name)
print(agent)
print(agent.lastname) #: Weldone

# Remember: all classes inherit from class object and this class include all specials method (__setattr__, __getattr__,…)

##issubclass and isinstance fonctions :
test = issubclass(SpecialAgentα, Person)
print(test)
test = issubclass(SpecialAgentα, object)
print(test)
test = issubclass(Person, object)
print(test)
test = issubclass(Person, SpecialAgentα)
print(test)

test = isinstance(agent, SpecialAgentα)
print(test)
test = isinstance(agent, Person)
print(test)

## Multiple Inherit
# syntax : class MyClass(MyMotherClass1, MyMotherClass2)
# order set is important to search methods:
# In MyClass else MyMotherClass1 else mothers classes of MyMotherClass1 else MyMotherClass2 else
# mothers classes of MyMotherClass2.

# Exceptions are classes
help(AttributeError)
# So AtthibuteError inherit form Exception which inherit from BaseExecption.
# when you get except TypeException, you will intercept all exceptions from TypeExecption and inherit classes of TypeException.
"""
 peut vous être utile de créer vos propres exceptions. Puisque les exceptions sont des classes, comme nous venons de le voir,
 rien ne vous empêche de créer les vôtres. Vous pourrez les lever avec raise, les intercepter avec except.

Se positionner dans la hiérarchie
Vos exceptions doivent hériter d'une exception built-in proposée par Python. Commencez par parcourir 
la hiérarchie des exceptions built-in pour voir si votre exception peut être dérivée d'une exception qui lui serait proche.
La plupart du temps, vous devrez choisir entre ces deux exceptions :

BaseException : la classe mère de toutes les exceptions.
 La plupart du temps, si vous faites hériter votre classe de BaseException, ce sera pour modéliser une exception 
 qui ne sera pas foncièrement une erreur, par exemple une interruption dans le traitement de votre programme.

Exception : c'est de cette classe que vos exceptions hériteront la plupart du temps. 
C'est la classe mère de toutes les exceptions « d'erreurs ».

Si vous pouvez trouver, dans le contexte, une exception qui se trouve plus bas dans la hiérarchie, c'est toujours mieux."""

# How to built your exception: You always need of __str__ method
class MyException(Exception):
  """Exception raised in one context… not difined here"""
  def __init__(self, message):
    """We just backup the error title"""
    self.message = message
  def __str__(self):
    """We return message"""
    return self.message

#decomment to raise the error check
#raise MyException("Oups… J'ai tout cassé")

class FileAnalysisError(Exception):
  """This exception is raised when a configuration file cannot be analysed.

  Attributs :
    file -- file mame
    line -- number of the line where we get error
    message -- what about the error"""
  
  def __init__(self, file, line, message):
    """Exception Constructor """
    self.file = file
    self.line = line
    self.message = message
  def __str__(self):
    """Print Exception"""
    return "[{}:{}]:{}".format(self.file, self.line, self.message)

#decomment to raise the error check
raise FileAnalysisError("plop.conf", 34, "bracket missing")

