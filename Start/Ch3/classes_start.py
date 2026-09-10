# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Vehicle:
  def __init__(self, make, bodystyle):
    self.make = make
    self.bodystyle = bodystyle
    
  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, engine, make, bodystyle):
    super().__init__(make, bodystyle)
    self.doors = 4
    self.wheels = 4
    self.engine = engine

  def drive(self, speed):
    super().drive(speed)
    print(f"the {self.make} car is driving at {self.speed} mph")

class Motorcycle(Vehicle):
  def __init__(self, engine, make, bodystyle):
    super().__init__(make, bodystyle)
    self.doors = 0
    self.wheels = 2
    self.engine = engine

  def drive(self, speed):
    super().drive(speed)
    print(f"the {self.make} motorcycle is driving at {self.speed} mph")
