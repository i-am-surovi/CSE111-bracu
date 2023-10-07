# Task 1

class Exams:
  def __init__(self, mark):
    self.mark = mark
  def __add__(self, obj):
    return Exams(self.mark+ obj.mark)

Q1 = Exams(int(input("Quiz 1 (out of 10): ")))
Q2 = Exams(int(input("Quiz 2 (out of 10): ")))
Lab = Exams(int(input("Lab (out of 30): ")))
Mid = Exams(int(input("Mid (out of 20): ")))
Final = Exams(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))

# Task 2

class Teacher:
  def __init__(self, name, department):
    self.__name = name
    self.__department = department
    self.__listCourse = []
  def addCourse(self, obj):
    n = obj.get()
    self.__listCourse.append(n)
  def printDetail(self):
    print("=======================================")
    print("Name: ",self.__name)
    print("Department: ",self.__department)
    print("List of Courses")
    print("=======================================")
    print(*self.__listCourse, sep="\n")
    print("=======================================")

class Course:
  def __init__(self, c_name):
    self.c_name = c_name
  def get(self):
    return self.c_name

t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CCSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()

# Task 3

# Player class
class Player:
  def __init__(self, player_name):
    self.p_name = player_name

# Team class
class Team:
  def __init__(self, team_name=None):
    self.__t_name = team_name
    self.__players = []
  def setName(self, team_name):
    self.__t_name = team_name
  def addPlayer(self, player):
    self.player = player
    self.__players.append(self.player.p_name)
  def printDetail(self):
    print("================================")
    print("Team: ", self.__t_name)
    print("List of Players:")
    print(self.__players)
    print("================================")

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()

# Task 4

class Color:
  def __init__(self, clr):
    self.clr = clr
  def __add__(self, obj):
    if (self.clr == 'red' and obj.clr == 'yellow') or (self.clr == 'yellow' and obj.clr == 'red'):
      return Color("Orange")
    elif (self.clr == 'red' and obj.clr == 'blue') or (self.clr == 'blue' and obj.clr == 'red'):
      return Color("Violet")
    elif (self.clr == 'yellow' and obj.clr == 'blue') or (self.clr == 'blue' and obj.clr == 'yellow'):
      return Color("Green")
    else:
      return Color("Wrong Color")

C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)

# Task 5

class Circle:
  def __init__(self, radius):
    self.__radius = radius
  def getRadius(self):
    return self.__radius
  def area(self):
    import math
    self.__area = math.pi*(self.getRadius()**2)
    return self.__area
  def __add__(self, obj):
    return Circle (self.getRadius() + obj.getRadius())
  def setRadius(self,new_radius):
    self.__radius = new_radius
    return self.__radius

c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" ,c1.area())

c2 = Circle(5)
print("Second circle radius:" ,c2.getRadius())
print("Second circle area:" ,c2.area())

c3 = c1 + c2
print("Third circle radius:" ,c3.getRadius())
print("Third circle area:" ,c3.area())

# Task 6

class Triangle:
  def __init__(self, base, height):
    self.__base = base
    self.__height = height
  def getBase(self):
    return self.__base
  def getHeight(self):
    return self.__height
  def __sub__(self,obj):
    return Triangle ((self.getBase() - obj.getBase()),(self.getHeight() - obj.getHeight()))
  def setBase(self, n_base):
    self.__base = n_base
    return self.__base
  def setHeight(self, n_height):
    self.__height = n_height
    return self.__height
  def area(self):
    return 0.5*self.getBase()*self.getHeight()

t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())

t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())

t3 = t1 - t2
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area())

# Task 7

class Dolls:
  def __init__(self, name, price, flag = False):
    self.name = name
    self.price = price
    self.flag = flag
  def detail(self):
    if self.flag == False:
      return f"Doll: {self.name}\nTotal Price: {self.price} taka"
    else:
      return f"Dolls: {self.name}\nTotal Price: {self.price} taka"
  def __gt__(self, obj):
    return self.price > obj.price
  def __add__(self, obj):
    return Dolls((self.name + obj.name),(self.price + obj.price),True)

obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

# Task 8

class Coordinates:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __sub__(self, obj):
    return Coordinates((self.x - obj.x),(self.y - obj.y))
  def __mul__(self,obj):
     return Coordinates((self.x * obj.x),(self.y * obj.y))
  def detail(self):
    return f"({self.x},{self.y})"
  def __eq__(self,obj):
    if (self.x == obj.x) and self.y==obj.y :
      return "The calculated coordinates are the same."
    else:
      return "The calculated coordinates are NOT the same."

p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))

p4 = p1 - p2
print(p4.detail())

p5 = p1 * p2
print(p5.detail())

point_check = (p4 == p5)
print(point_check)
