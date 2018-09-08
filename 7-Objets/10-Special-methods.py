#!/usr/bin/python3
# -*-coding:utf-8 -*

class Person:
  """ Class to picture a person """
  def __init__(self, name, last_name): # First sepcial method (as __get__ and __set__ and __del__)
    """ constructor """
    self.name = name
    self.last_name = last_name
    self.age = 33
  def __repr__(self): # allow to represent your object in your way: usefull for Debug-log.
    """ when you enter in the object with interpretor """
    return "Person: name({}), last_name({}), age({})".format(
      self.name, self.last_name, self.age
    )
  def __str__(self): # very similar with the last method : convert the object representation in string
    return "{} {}, is {} year old".format(self.name, self.last_name, self.age)

p1 = Person("Manson", "Marylin")
print(p1) # use __repr__ when you want printing the object
print(repr(p1)) # internal function : idem than just before.
string = str(p1)
print(string) 
# you can see twice because __repr__ involves __str__ (similar method)
""" Result:
root@SurfaceVincent:/mnt/c/Users/Vincent/Documents/dev/comparaison_de_codes/7-Objets# python3 10-Special-methods.py
Manson Marylin, is 33 year old
Person: name(Manson), last_name(Marylin), age(33)
Manson Marylin, is 33 year old
"""
# __getattr__
class Protected:
  """ Class with special method getting attributs :
      if the attribut is not found, we print an alert and return none """
  
  def __init__(self):
    """We create some default attributs """
    self.a = 1
    self.b = 2
    self.c = 3
  def __getattr__(self, name):
    """If Python does not find the name attribut, it get this method.
    We print an alert """

    print("Alert ! There is no attribut {} here !".format(name))

pro = Protected()
print(pro.a)
print(pro.c)
test = pro.e
print(test)
"""Result :
1
3
Alert ! There is no attribut e here !
None
"""

# __setattr__ : Define the attribute access to modify this attribute.
"""
  def __setattr__(self, attr_name, attr_value):
    # method called when we do obj.attr_name = attr_value.
    # Then we record the objk

    object.__setattr__(self, attr_name, attr_value)
    self.save()
    # To understant object. We need to refere to inheritance.
    # you cannot redifine self.attr_name = attr_value because you would create infinite loop (because this method call __setattr__ of your class)
"""
# __delattr__: Define how to manage when we want delete an attribute.
"""
  def __delattr__(self, attr_name):
    # we don't want to allow attr_name deletion.

    raise AttributError("Error: You can not destroy this class attribut")
    
    # you cannot redifine by del self.attr_name because you would create infinite loop to.
  
"""

# Function that make the same job as class method
myObject = Protected()
print(getattr(myObject, "a")) # it is the same as myObject.a
setattr(myObject, "b", 5) # it is similar to myObject.b = 5
print(getattr(myObject, "b"))
delattr(myObject, "c") # it is similar to del object.c or object.__delattr__("c")
print(hasattr(myObject, "d")) # Return True if the attribute "d" exist, false neither.
"""Result:
1
5
True --> I don't understand for now.
"""
# Container methods
#Container objects contains other object (like String chain, list, dictionaries)
#You can access to the contains with [] symbol.
# Then we can modify how to work with:
# myObject[index] : __getitem__
# myobject[index] = value : __setitem__
# del myObject[index] : __delitem__
# we will make an object similar to a dictionnary (but it will not) 
class ZDict:
  """ Class like a dictionary """
  def __init__(self):
    """ our class does not have any parameters """
    self._dictionary = {} # crée l'enveloppe
  def __getitem__(self, index):
    """ This special method is called when we do myObject[index] """
    return self._dictionary[index]
  def __setitem__(self, index, value):
    """ This special method is called when we do myObject[index] = value """
    self._dictionary[index] = value + 1
  def __contains__(self, value):
    """ This special method is called when we do value in myObject """
    return self._dictionary.__contains__(value) # Return True or False
  def __len__(self):
    """ This special method is called when we use len fonction on the object """
    return self._dictionary.__len__()

test = ZDict()
test[0] = 0
test[1] = 1
print(test[0])
print(0 in test)
print("contenu de test:", test)
print(dir(test))
print(len(test))
""" Results: 
1
True
contenu de test: <__main__.ZDict object at 0x7fc3bc930b00>
['__class__', '__contains__', '__delattr__', '__dict__', '__dir__',…

"""
# Maths Methods
class Duration:
  """ Class with duration in minutes, secondes format """

  def __init__(self, min=0, sec=0):
    """ Constructor """
    self.min = min
    self.sec = sec
  def __str__(self):
    """ Print pretty format for our objects """
    return "{0:02}:{1:02}".format(self.min, self.sec)

d1 = Duration(3,5)
print(d1)
""" Result :
03:05
"""
#You cannot do d1 + 4 for exemple
# you have to (re)define the __add__ method for this object
# d1 + 4 is similar to d1.__add__(4)
# if you need to do different actions according to the object type,
# you have to test the object type with type(object_to_add)
class Duration2:
  """ Class with duration in minutes, secondes format """

  def __init__(self, min=0, sec=0):
    """ Constructor """
    self.min = min
    self.sec = sec
  def __str__(self):
    """ Print pretty format for our objects """
    return "{0:02}:{1:02}".format(self.min, self.sec)
  def __add__(self, object_to_add):
    """ The object to add is an int, the number in secondes"""
    new_duration = Duration2()
    # We backup self in the object to have the same duration
    new_duration.min = self.min
    new_duration.sec = self.sec
    # We add the duration
    new_duration.sec += object_to_add
    # if second number is >= 60
    if new_duration.sec >= 60:
      new_duration.min += new_duration.sec // 60
      new_duration.sec = new_duration.sec % 60
    # new duration
    return new_duration
  def __iadd__(self, object_to_add):
    """ special method for «+=» operator, The object to add is an int, the number of seconds """
    # we work with self this time
    # we add the duration
    self.sec += object_to_add
    if self.sec >= 60:
      self.min += self.sec // 60
      self.sec = self.sec % 60
    return self

d1 = Duration2(12, 8)
print(d1)
d2 = d1 + 54 # d1 + 54 seconds
print(d2)
d2 += 128
print(d2)
# carefull, d1 + 54 is different from 54 + d1, indeed d1 + is like d1.__add__(54)

""" others :
__sub__: surcharge de l'opérateur-;
__mul__: surcharge de l'opérateur*;
__truediv__: surcharge de l'opérateur/;
__floordiv__: surcharge de l'opérateur//(division entière) ;
__mod__: surcharge de l'opérateur%(modulo) ;
__pow__: surcharge de l'opérateur**(puissance) ;
…
"""


