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


