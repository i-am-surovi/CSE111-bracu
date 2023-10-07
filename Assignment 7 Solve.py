# Task 1

class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name
        self.__department = dept
    def set_department(self, dept):
        self.__department = dept
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def __str__(self):
        return 'Name: '+self.__name+' Department: '+self.__department

class BBA_Student(Student):
  def __init__(self, name = "default", dept = "BBA"):
    super().__init__(name,"BBA")

print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))

# Task 2

class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def moveUp(self):
        self.y += 1
    def moveDown(self):
        self.y -= 1
    def moveRight(self):
        self.x += 1
    def moveLeft(self):
        self.x -= 1
    def __str__(self):
        return '('+str(self.x)+' , '+str(self.y)+')'

class Vehicle2010(Vehicle):
    def moveLowerLeft(self):
        super().moveDown()
        super().moveLeft()
    def moveUpperRight(self):
        super().moveUp()
        super().moveRight()
    def moveUpperLeft(self):
        super().moveUp()
        super().moveLeft()
    def moveLowerRight(self):
        super().moveDown()
        super().moveRight()

    def equals(self, other):
        return self.x == other.x and self.y == other.y

print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))

# Task 3

class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

class Cricket_Tournament(Tournament):
    def __init__(self, name="Default", teams=0, types="No type"):
      super().__init__(name)
      self.teams = teams
      self.types = types

    def detail(self):
        n = super().get_name()
        return f"Cricket Tournament Name: {n}\nNumber of Teams: {self.teams}\nType: {self.types}"


class Tennis_Tournament(Tournament):
    def __init__(self, name, player_num):
        super().__init__(name)
        self.player_num = player_num

    def detail(self):
        return f"Tennis Tournamnet Name: {super().get_name()}\nNumber of Players: {self.player_num}"


ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())

# Task 4

class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+"Price: "+str(self.__price)

class Book(Product):
    def __init__(self, id, title, price, ISBN, publisher):
        super().__init__(id, title, price)
        self.ISBN = ISBN
        self.publisher = publisher

    def printDetail(self):
        return super().get_id_title_price()+ f"\nISBN: {self.ISBN} Publisher: {self.publisher}"


class CD(Product):
    def __init__(self, id, title, price, band, duration, genre):
        super().__init__(id, title, price)
        self.band = band
        self.duration = duration
        self.genre = genre

    def printDetail(self):
        return super().get_id_title_price()+ f"\nBand: {self.band} Duration: {self.duration} minutes\nGenre: {self.genre}"

book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())

# Task 5

class Animal:
    def __init__(self,sound):
        self.__sound = sound

    def makeSound(self):
        return self.__sound

class Printer:
    def printSound(self, a):
        print(a.makeSound())

class Dog(Animal):
    def __init__(self, sound):
        super().__init__(sound)


class Cat(Animal):
    def __init__(self, sound):
        super().__init__(sound)

d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)

# Task 6

class Shape:

  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: " + str(self.height) + ",Base: " + str(self.base)


class triangle(Shape):
    def calcArea(self):
        self.area = (self.height * self.base) / 2

    def printDetail(self):
        return f"Shape name: {self.name}\n" + super().get_height_base() + f"\nArea: {self.area}"

class trapezoid(Shape):
    def __init__(self, name, height, base, side_A):
        super().__init__(name, height, base)
        self.side_A = side_A

    def calcArea(self):
        self.area = ((self.base + self.side_A) / 2) * self.height

    def printDetail(self):
        return f"Shape name: {self.name}\n" + super().get_height_base() + f", Side_A: {self.side_A}" + f"\nArea: {self.area}"

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())

# Task 7

class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(SportsPerson):
    def __init__(self, team_name, name, role, goal, played):
        super().__init__(team_name, name, role)
        self.goal = goal
        self.played = played

    def calculate_ratio(self):
        self.ratio = self.goal / self.played

    def print_details(self):
        earning = (self.goal * 1000) + (self.played * 10)
        print(super().get_name_team())
        print(f"Team Role: {self.role}")
        print(f"Total Goal: {self.goal}, Total Played: {self.played}")
        print(f"Goal Ratio: {self.ratio}")
        print(f"Match Earning: {earning}K")

class Manager(SportsPerson):
    def __init__(self, team_name, name, role, win):
        super().__init__(team_name, name, role)
        self.win = win

    def print_details(self):
        earning = self.win * 1000
        print(super().get_name_team())
        print(f"Team Role: {self.role}")
        print(f"Win: {self.win}")
        print(f"Match Earning: {earning}K")

player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
