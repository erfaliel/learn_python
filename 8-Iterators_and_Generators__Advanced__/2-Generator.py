#!/usr/bin/python3
# -*-coding:utf-8 -*

# Basic example
def my_generator():
  """Our first generator. It just return 1, 2, 3"""
  yield 1
  yield 2
  yield 3

print(my_generator)
print(my_generator())
my_iterator = iter(my_generator())
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
"""result:
1
2
3"""
#print(next(my_iterator)) # you must get
#when we call "next", out function which use to iter, execute and stop
# at the first instruction yield and remember this location and so on.
# so this generator build a python object which define its own __iter__ special method
#We can use :
for number in my_generator(): # it's necessary to execute the function()
  print(number)
"""result:
1
2
3"""

def my_range(a, b):
  """a and b define range to print"""
  a += 1
  while a < b:
    yield a
    a += 1
  #raise StopIteration it's not necessary !
for number in my_range(5, 10):
  print(number)

# we can reuse generators to reverse String
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
  print(char)

# generator and coroutins
# you can change behaviors during iteration
# ... like break a loop
My_new_generator = my_range(5, 20) # First we have to exec the generator and put it into a var  
for number in My_new_generator: # we cannot do or number in my_range(5, 20) 
  if number > 17:
    My_new_generator.close() # Stop the loop
  print(number)

""" Result :
6
7
8
9
10
11
12
13
14
15
16
17
18"""

# We can send datas to generator during execution
def my_range(a, b):
  """Generatou that is crossing an int serie from a to b.
  Our generator has to bypass a range of int according to a value.
  this value become the new 'a' value.

  a must be smaller than b. """

  a += 1
  while a < b:
    received_value = (yield a)
    if received_value is not None: # Our generatou has received something
      a = received_value
    a += 1

# this is the code to intetact with the generator
my_generator = my_range(10, 25)
for number in my_generator:
  if number == 15:
    my_generator.send(20)
  print(number, end=" ")




