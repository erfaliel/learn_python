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




