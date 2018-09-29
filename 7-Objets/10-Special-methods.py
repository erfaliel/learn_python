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
  def __eq__(self, object_to_compare):
    """ Test if attributes of self and object_to_compare are equal """
    return self.min == object_to_compare.min and self.sec == object_to_compare.sec
  def __gt__(self, object_to_compare):
    """ Test if attributes of self is greater than attributes of object_to_compare """
    number_of_sec_object1 = self.sec + (self.min * 60)
    number_of_sec_object2 = object_to_compare.sec + (object_to_compare.min * 60)
    return number_of_sec_object1 > number_of_sec_object2

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
# Compare methods:
# Allow to compare two objects with each other
"""
== def __eq__(self, objet_a_comparer):Opérateur d'égalité (equal). RenvoieTruesiselfetobjet_a_comparersont égaux,False sinon.
!= def __ne__(self, objet_a_comparer):Différent de (non equal). RenvoieTruesiselfetobjet_a_comparersont différents,False sinon.
>  def __gt__(self, objet_a_comparer):Teste siselfest strictement supérieur (greater than) àobjet_a_comparer.
>= def __ge__(self, objet_a_comparer):Teste siselfest supérieur ou égal (greater or equal) àobjet_a_comparer.
<  def __lt__(self, objet_a_comparer):Teste siselfest strictement inférieur (lower than) àobjet_a_comparer.
<= def __le__(self, objet_a_comparer):Teste siselfest inférieur ou égal (lower or equal) àobjet_a_comparer.
"""
d1 = Duration2(12, 8)
d2 = Duration2(5, 3)
print(d1 == d2) # False
print(d1 > d2)  # True

# Special methods for Pickler (record object in file).
import pickle
class Temp:
  """ Class with 3 attributes including 1 temporary """
  def __init__(self):
    """Constructor """
    self.attribut_1 = "A value"
    self.attribut_2 = "Another value"
    self.temp_attribut = 5
  def __getstate__(self):           # Called just before you are serializing object in order to record it
    """Return attributs dictionnary to serialize """
    dict_attr = dict(self.__dict__) # affectation by reference in this case
    dict_attr["temp_attribut"] = 0  # then temp_attribut changed only in dict_attr object
    return dict_attr

  # Here another method to achieve the same goal in a different way (but __setstate__ and __getstate__ could exist both togather) 
  # def __setstate__(self, dict_attr):           # Called just after deserialized your object to load it.
  #  """ Method called during object deserialization """
  #  dict_attr["temp_attribut"] = 0
  #  return dict_attr

print(Temp().attribut_2) # Another value
MyTempObject = Temp()
print("Attributs are attribut_1 : {}, attribut_2 : {}, temp_attribut : {}".format(
  MyTempObject.attribut_1,
  MyTempObject.attribut_2,
  MyTempObject.temp_attribut)) # Attributs are attribut_1 : A value, attribut_2 : Another value, temp_attribut : 5

with open('object_file', 'wb') as object:
  my_pickler = pickle.Pickler(object)
  my_pickler.dump(MyTempObject)

with open('object_file', 'rb') as file:
  my_depickler = pickle.Unpickler(file)
  MyTempObjectRecorded = my_depickler.load()

print("My recorded object is : {}".format(MyTempObjectRecorded)) # My recorded object is : <__main__.Temp object at 0x…
print("Attributs are attribut_1 : {}, attribut_2 : {}, temp_attribut : {}".format(
  MyTempObjectRecorded.attribut_1,
  MyTempObjectRecorded.attribut_2,
  MyTempObjectRecorded.temp_attribut)) # Attributs are attribut_1 : A value, attribut_2 : Another value, temp_attribut : 0
