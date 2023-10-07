# Task 1

class Student:
  ID = 0

  def __init__(self, name, department, age, cgpa):
    self.name = name
    self.department = department
    self.age = age
    self.cgpa = cgpa

  def showDetails(self):
    Student.ID += 1
    print("ID:",Student.ID)
    print("Name:",self.name)
    print("Department:",self.department)
    print("Age:",self.age)
    print("CGPA:",self.cgpa)

  @classmethod
  def from_String(cls, all):
    name,department,age,cgpa = all.split("-")
    return Student(name, department, age, cgpa)

s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()

# Quesiton -1
print("Changing the class variable value will also change all the instance value that inherited the same variable from the class")
print("But changing a instance variable will only change the varialbe value inside of that specific instance\n")

# Quesiotn -2
print("Instance methods cannot be accessed without the instance of that class, but class methods don't need a instance to be used")

# Task 2

class Assassin:
  total = 0
  def __init__(self, name, per):
    self.name = name
    self.per = per

  def printDetails(self):
    Assassin.total += 1
    print("Name:",self.name)
    print("Success rate:",self.per,"%")
    print("Total number of Assassin:",Assassin.total)

  @classmethod
  def failureRate(cls, name, per):
    s_per = 100 - per
    return Assassin(name, s_per)

  @classmethod
  def failurePercentage(cls, name, str):
    s_per = 100 - int(str[:len(str)-1])
    return Assassin(name, s_per)

john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('================================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('================================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()

# Task 3

class Passenger:
  count = 0

  def __init__(self, name):
    self.name = name
    self.fair = 450

  def set_bag_weight(self,weight):
    if weight <= 20:
      self.fair += 0
    elif 21 <= weight <= 50:
      self.fair += 50
    else:
      self.fair += 100

  def printDetail(self):
    Passenger.count += 1
    print("Name:",self.name)
    print("Bus Fare:",self.fair,"taka")

print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)

# Task 4

class Travel:
  count = 0

  def __init__(self, source, destination):
    self.source = source
    self.destination = destination
    self.time = "1:00"

  def display_travel_info(self):
    Travel.count += 1
    return f"Source:{self.source}\nDestination:{self.destination}\nFlight Time:{self.time}"

  def set_time(self, t):
    t = str(t)
    self.time = t + ":00"

  def set_destination(self, d):
    self.destination = d

  def set_source(self, s):
    self.source = s

print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)

# Task 5

class Employee:
  def __init__(self, name, workingPeriod):
    self.name = name
    self.workingPeriod = workingPeriod

  @classmethod
  def employeeByJoiningYear(cls, name, year):
    exp = 2022 - year
    return Employee(name, exp)

  @staticmethod
  def experienceCheck(wp, g):
    if g == "male":
      if wp < 3:
        return "He is not experienced"
      else:
        return "He is experienced"
    elif g == "female":
      if wp < 3:
       return "She is not experienced"
      else:
        return "She is experienced"

employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))

# Task 6

class Laptop:
  laptopCount = 0
  def __init__(self, name, count):
    Laptop.laptopCount += count
    self.name = name
    self.count = count

  @classmethod
  def resetCount(cls):
    cls.laptopCount = 0

  @classmethod
  def advantage(cls):
    print("Laptops are portable")

lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)

# Task 7

class Cat:
  Number_of_cats = 0

  def __init__(self, name, work):
   Cat.Number_of_cats += 1
   self.name = name
   self.work = work

  def changeColor(self, name):
    self.name = name

  def printCat(self):
    print(f"{self.name} cat is {self.work}")

  @classmethod
  def no_parameter(cls):
    name = "White"
    work = "Sitting"
    return Cat(name,work)

  @classmethod
  def first_parameter(cls, name):
    work = "sitting"
    return Cat(name,work)

  @classmethod
  def second_parameter(cls, work):
    name = "Grey"
    return Cat(name, work)

print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)

# Task 8

import math
class Cylinder:
  radius = 5
  height = 18

  def __init__(self, radius, height):
    print("Default radius=", Cylinder.radius, "and height=", Cylinder.height)
    Cylinder.radius = radius
    Cylinder.height = height
    print("Updated radius=", Cylinder.radius, "and height=", Cylinder.height)

  @classmethod
  def swap(cls, height, radius):
    return cls(radius, height)

  @classmethod
  def changeFormat(cls, st):
    lst = st.split("-")
    radius = float(lst[0])
    height = float(lst[1])
    return cls(radius, height)

  @staticmethod
  def area(radius, height):
    ar = 2 * math.pi * radius * radius + 2 * math.pi * radius * height
    print("Area:", ar)

  @staticmethod
  def volume(radius, height):
    vol = math.pi * radius * radius * height
    print("Volume:", vol)

c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)

# Task 9

class Student:
  t_s = 0
  b_s = 0
  o_s = 0

  @classmethod
  def printDetails(cls):
    print("Total Student(s):",cls.t_s)
    print("BRAC University Student(s):",cls.b_s)
    print("Other Institution Student(s):",cls.o_s)

  def __init__(self, name, dept, inst = "BRAC University"):
    self.name = name
    self.dept = dept
    self.inst = inst
    Student.t_s += 1
    if self.inst == "BRAC University":
      Student.b_s += 1
    else:
      Student.o_s += 1

  def individualDetail(self):
    print("Name:",self.name)
    print("Department:",self.dept)
    print("Institution:",self.inst)

  @classmethod
  def createStudent(cls, name, dept, inst = "BRAC University"):
    cls.name = name
    cls.dept = dept
    cls.inst = inst
    return Student(cls.name,cls.dept,cls.inst)

Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()

# Task 10

class SultansDine:
  total_branch = 0
  total_sell = 0
  branch_info = []

  def __init__(self, branch):
      self.name = branch
      SultansDine.total_branch += 1

  def sellQuantity(self, quantity):
    if quantity < 10:
      self.branch_sell = quantity * 300
    elif quantity < 20:
      self.branch_sell = quantity * 350
    else:
      self.branch_sell = quantity * 400

    SultansDine.total_sell += self.branch_sell

  def branchInformation(self):
      print(f"Branch Name: {self.name}")
      print(f"Branch Sell: {self.branch_sell}")

      SultansDine.branch_info.append(self.name)
      SultansDine.branch_info.append(self.branch_sell)

  @classmethod
  def details(cls):
      print(f"Total Number of branch(s): {cls.total_branch}")
      print(f"Total Sell: {cls.total_sell}")

      for index in range(0, len(SultansDine.branch_info), 2):
        print(f"Branch Name: {SultansDine.branch_info[index]}, Branch Sell: {SultansDine.branch_info[index + 1]} Taka")
        print(f"Branch consists of total sell's: {(SultansDine.branch_info[index + 1] / SultansDine.total_sell) * 100:.2f}%")

SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()

# Task 11 (Tracing)

class Puzzle:
  x = 0
  def methodA(self):
    Puzzle.x = 5
    z = Puzzle.x + self.methodB(Puzzle.x)
    print(Puzzle.x, z)
    z = self.methodB(z + 2) + Puzzle.x
    print(Puzzle.x, z)
    self.methodB(Puzzle.x, z)
    print(Puzzle.x, z)
  def methodB(self, *args):
    if len(args) == 1:
      y = args[0]
      Puzzle.x = y + Puzzle.x
      print(Puzzle.x, y)
      return Puzzle.x + 3
    else:
      z, x = args
      z = z + 1
      x = x + 1
      print(z, x)

p = Puzzle()
p.methodA()
# p.methodA()
# p = Puzzle()
# p.methodA()
# p.methodB(7)
