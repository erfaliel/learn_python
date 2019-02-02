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
  
def my_decorator2(function):
  """Our decorator : it will print a message before to call the function"""
  def modified_function():
    """This is the function that we will return. It is a little bit modified function.
    we just want to print a message before to run our first function."""

    print("Carefull ! We call {0}".format(function))
    return function() # execute the function in parameter ant retunn the result (no result here, because print doesn't return value)
  return modified_function # return the upgraded function

print("How to modify the function behaviour part 1")
@my_decorator2 # we bind hello() to my decorator2
def hello():
  print("Hello !")

# Test:
hello() # So here Python returns the modified_function
print(hello) # here you can see what function is called by python
""" Result:
How to modify the function behaviour part 1
Carefull ! We call <function hello at 0x7f3d48318d08>
Hello !
<function my_decorator2.<locals>.modified_function at 0x7f3d48318d90>
"""

# decorator with parameters

""" in this case we have:
@my_decorator(parameter)
def function(...):
  ...
is the same as:

def function(...):
  ...

function = my_decorator(parameter)(function)
"""
""" to deal with time, we are going to import the time module"""
import time

def time_controler(nb_secs): # Parameter level of the decorator
  """ check the function execution time.
  if the time exceed nb_secs, we print an alert."""

  def my_decorator3(function_to_execute): # Decorator definition level
    """Our decorator. it is called when we will define our function to execute"""

    def modified_function3(): # modification level
      """Returned function from the the decorator. it manages time calculation to 
      of the function_to_execute"""

      top_start = time.time() # before to execute our function
      value_to_return = function_to_execute() # => we execute the effective function
      top_end = time.time()
      execution_time = top_end - top_start
      if execution_time >= nb_secs:
        print("The execution time of function {0} was {1} secs".format( \
                function_to_execute, execution_time))
      return value_to_return
    return modified_function3
  return my_decorator3

# Here we start using time_controller definition
@time_controler(5)
def wait():
  input("press Enter Key...")
# Here start the program
wait()  # Here try to press enter before 5 secs
wait()  # Here try to press enter after 5 secs and compare the result

"""Result you should get :
press Enter Key...
press Enter Key...
The execution time of function <function wait at 0x7f5478a74048> was 8.38449239730835 secs
"""

# Decorator on funcion with parameters
"""If our function is build with parameters, then the modified function needs to get these paramters
But, decorator can use different function with no or some parameters, so we can use :
"""
import time

def time_controler4(nb_secs): # Parameter level of the decorator
  """ check the function execution time.
  if the time exceed nb_secs, we print an alert."""

  def my_decorator4(function_to_execute): # Decorator definition level
    """Our decorator. it is called when we will define our function to execute"""

    def modified_function4(*unamed_parameters, **named_parameters): # modification level
      """Returned function from the the decorator. it manages time calculation to 
      of the function_to_execute"""

      top_start = time.time() # before to execute our function
      value_to_return = function_to_execute(*unamed_parameters, **named_parameters) # => we execute the effective function
      top_end = time.time()
      execution_time = top_end - top_start
      if execution_time >= nb_secs:
        print("The execution time of function {0} was {1} secs".format( \
                function_to_execute, execution_time))
      return value_to_return
    return modified_function4
  return my_decorator4

# Here we start using time_controller definition
@time_controler4(5)
def wait2(start_parameter, end_parameter):
  print(start_parameter)
  input("press Enter Key...")
  print(end_parameter)
# Here start the program
wait2("Hello", "world" )  # Here try to press enter before 5 secs
wait2("Salut", "Tout le monde")  # Here try to press enter after 5 secs and compare the result

""" Result you should get :
Hello
press Enter Key...
world
Salut
press Enter Key...
Tout le monde
The execution time of function <function wait2 at 0x7feaab5c6268> was 7.083711624145508 secs
"""




  

