import math

pi = math.pi

class Rectangle:
  def __init__(self, height, width):
    self.h = height
    self.w = width

  def perimeter(self):
    return (self.h + self.w) * 2
  def area(self):
    return self.h * self.w

class Circle:
  def __init__(self, radius):
    self.r = radius

  def perimeter(self):
    return 2 * pi *self.r
  def area(self):
    return pi * self.r * self.r
  
