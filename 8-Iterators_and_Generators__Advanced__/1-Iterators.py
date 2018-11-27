#!/usr/bin/python3
# -*-coding:utf-8 -*

# Basic Iterator
my_liste = [1, 2, 3]
for element in my_liste:
  print(element)
my_Charlist = "test"
iterator_from_my_charlist = iter(my_Charlist) #Fonction to call method __iter__ from object passed in parameter
print(next(iterator_from_my_charlist))        #Fonction to call method __next__ return next element of the iterator.
print(next(iterator_from_my_charlist))
print(next(iterator_from_my_charlist))
print(next(iterator_from_my_charlist))
# print(next(iterator_from_my_charlist))      # Exception to mark the end of the iterator
# this the way used by for instruction (char, list, dict)

# We can redifine the management
class RevStr(str):
  """Class inherits from str object:
  Here we are going to change the way to cross an str object (from right to left)

  Others methods, constructor included don't need to be redefined."""

  def __iter__(self):
    """This method return a new iterator"""

    return ItRevStr(self) # So __iter__ run ItRevStr object
 
class ItRevStr:
  """An Iterator that reverses how to work 'str'.
  We record location attribut of the char to cross."""
  def __init__(self, string_to_cross):
    """We set location to the end of the string"""
    self.string_to_cross = string_to_cross
    self.location = len(string_to_cross)
  def __next__(self):
    """This method must return the next element of the string
    or raise an exception 'StopIteration' if it reach the end of the string.
    We must stick to this way according to iterator rules (__next__ method, 'StopIteration' exception '')"""

    if self.location == 0: # End of the way
      raise StopIteration
    self.location -= 1 # Decrease location
    return self.string_to_cross[self.location] # Return current char

my_string = RevStr("Bonjour")
print(my_string)
for element in my_string: # basic for loop
  print(element)
#We should see how works the for loop on RevStr object.
