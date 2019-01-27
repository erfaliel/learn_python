#!/usr/bin/python3
# -*-coding:utf-8 -*

# basic Decorator
def my_decorator(function):
  """First example of decorator"""
  print("Our decorator is called with the {0} function".format(function))
  return function

@my_decorator #The decorator is execute at this point to modify the salut function
def salut():
  """"Function modified by our decorator"""
  print("Salut !")

  """Result :
  Our decorator is called with the <function salut at 0x7f0e1b318bf8> function
  """

  # we can write :
  #   @my_decorator
  #   def my_function(...):
  #     ...
  #   or
  #   def my_function(...):
  #     ...
  #   my_function = my_decorator(my_function)  

  # How to modify the function behaviour
  



