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

print("Compteur d'objet créés: {}. ".format(counter.created_object))
object_1 = counter()
print("create first object : {}. ".format(object_1))
print("Compteur d'objet créés: {}. ".format(counter.created_object))
object_2 = counter()
print("create seconde object : {}. ".format(object_2))
print("Compteur d'objet créés: {}. ".format(counter.created_object))

print("Donc l'attribut «created_object» (un compteur) est lié à la classe et non à l'objet venant d'être créé. ")