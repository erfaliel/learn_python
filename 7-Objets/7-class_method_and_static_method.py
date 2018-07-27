#!/usr/bin/python3
# -*-coding:utf-8 -*

class counter:
  """Class with an attribute which increment each time a new object is created
     with this class. """
  
  created_object = 0 # initilizing count
  def __init__(self):
    """ Each time we created a new object, we will increment counter,
        because, attribute created_object belongs to the class (not into the constructor of the object) """
    counter.created_object += 1 # in this case we have to put the class_name before the attribute (it is into class, not in the self creating object)
  def how_many(cls):  # cls for class this time
    """ Class method to print how many object are created by the class """
    print("So far, {} objects are created.".format(
      cls.created_object
    ))
  how_many = classmethod(how_many) # to recognize and convert in class method when we need to call it

counter.how_many()
a = counter()
counter.how_many()
b = counter()
counter.how_many()

# find and create static method
class Pizza:
  """ Method static test """
  def mix_ingredients(x, y):
    return x + y
  
  def cook(self):
    return self.mix_ingredients(self.cheese, self.vegetables)
  mix_ingredients = staticmethod(mix_ingredients)

print(Pizza().cook is Pizza().cook) # 2 objects instanced so cook is dependant of each object.
print(Pizza().mix_ingredients is Pizza().mix_ingredients) # 1 object instanced and compared method of the class 
#                                                   method of the object
print(Pizza.mix_ingredients is Pizza().mix_ingredients) # 2 objects instanced but this static method is the same
#                                                  because bind to the  class