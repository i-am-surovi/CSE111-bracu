# Task 01

class RealNumber:

    def __init__(self, r=0):
        self.__realValue = r
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self, r):
        self.__realValue = r
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())

class ComplexNumber(RealNumber):
    def __init__(self, r=1, i=1):
        super().__init__(float(r))
        self.imaginary_Value = float(i)

    def __str__(self):
        return f"RealPart: {self.getRealValue()}\nImaginaryPart: {self.imaginary_Value}"

cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)

# task 02

class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)

class ComplexNumber(RealNumber):
    def __init__(self, real, imaginary):
        if isinstance(real, int):
            super().__init__(real)
            self.imaginary = imaginary
        else:
            super().__init__(real.number)
            self.imaginary = imaginary

    def __add__(self, obj):
        return ComplexNumber((self.number + obj.number), (self.imaginary + obj.imaginary))

    def __sub__(self, obj):
      return ComplexNumber((self.number - obj.number), (self.imaginary - obj.imaginary))

    def __str__(self):
        if self.imaginary < 0:
            return f"{str(self.number) + str(self.imaginary)}i"
        else:
            return f"{self.number} + {self.imaginary}i"

r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)

# task 03

class Account:
    def __init__(self, balance):
        self._balance = balance
    def getBalance(self):
        return self._balance

class CheckingAccount(Account):
    numberOfAccount = 0
    def __init__(self, balance=0.0):
        CheckingAccount.numberOfAccount += 1
        super().__init__(balance)
    def __str__(self):
        return f"Account Balance: {str(self.getBalance())}"

print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: ', CheckingAccount.numberOfAccount)

# Task 04

class Fruit:
    def __init__(self, formalin=False, name=''):
        self.__formalin = formalin
        self.name = name

    def getName(self):
        return self.name

    def hasFormalin(self):
        return self.__formalin

class testFruit:
    def test(self, f):
        print('----Printing Detail----')
        if f.hasFormalin():
            print('Do not eat the',f.getName(),'.')
            print(f)
        else:
            print('Eat the',f.getName(),'.')
            print(f)

class Mango(Fruit, testFruit):
    def __init__(self, name="Mango", formalin=True):
        super().__init__(formalin, name)

    def __str__(self):
        if self.hasFormalin():
            return f"{self.getName()}s are bad for you"
        else:
            return f"{(self.getName())}s are good for you"

class Jackfruit(Fruit, testFruit):
    def __init__(self, name="Jackfruit", formalin=False):
        super().__init__(formalin, name)

    def __str__(self):
        if self.hasFormalin():
            return f"{self.getName()}s are bad for you"
        else:
            return f"{(self.getName())}s are good for you"

m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)

# Task 05

class Exam:
    def __init__(self, marks):
        self.marks = marks
        self.time = 60

    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"

class ScienceExam(Exam):
    def __init__(self, marks, time, *subjects):
        super().__init__(marks)
        self.time = time
        self.lst_subjects = []
        self.var = 2
        for i in subjects:
            self.var += 1
            self.lst_subjects.append(i)

    def examSyllabus(self):
        sub_list = super().examSyllabus()
        for i in self.lst_subjects:
            sub_list += " , " + i
        return sub_list

    def examParts(self):
        var = super().examParts()
        counter = 3
        for i in self.lst_subjects:
            var += f"part {str(counter)} - {i}\n"
            counter += 1
        return var

    def __str__(self):
        return f"Marks: {self.marks} Time: {self.time} Number of Parts: {self.var}"

engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print("----------------------------------")
print(engineering.examSyllabus())
print(engineering.examParts())
print("==================================")
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print("----------------------------------")
print(architecture.examSyllabus())
print(architecture.examParts())

# Task 06

class Shape3D:
    pi = 3.14159

    def __init__(self, name="Default", radius=0):
        self._area = 0
        self._name = name
        self._height = "No need"
        self._radius = radius

    def calc_surface_area(self):
        return 2 * Shape3D.pi * self._radius

    def __str__(self):
        return "Radius: " + str(self._radius)

class Sphere(Shape3D):
    def __init__(self, name, radius):
        super().__init__(name, radius)
        print(f"Shape name: {self._name} Area Formula: 4*pi*r*r")

    def calc_surface_area(self):
        self._area = 4 * Shape3D.pi * self._radius * self._radius
        return self._area

    def __str__(self):
        return f"Radius: {str(self._radius)} Height: {str(self._height)}\nArea: {str(self._area)}"

class Cylinder(Shape3D):
    def __init__(self, name="Cylinder", radius=0, height=0):
        super().__init__(name, radius)
        print(f"Shape name: {str(self._name)} Area Formula: 2*pi*r*(r+h)")
        self._height = height

    def calc_surface_area(self):
        self._area = 2 * Shape3D.pi * self._radius * (self._radius + self._height)
        return self._area

    def __str__(self):
        return f"Radius: {str(self._radius)} Height: {str(self._height)}\nArea: {str(self._area)}"

sph = Sphere("Sphere", 5)
print("----------------------------------")
sph.calc_surface_area()
print(sph)
print("==================================")
cyl = Cylinder("Cylinder", 5, 10)
print("----------------------------------")
cyl.calc_surface_area()
print(cyl)

# Task 07

class PokemonBasic:
    def __init__(self, name="Default", hp=0, weakness="None", type="Unknown"):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type

    def get_type(self):
        return "Main type: " + self.type

    def get_move(self):
        return "Basic move: " + "Quick Attack"

    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness

class PokemonExtra(PokemonBasic):
    def __init__(self, name="Defalut", hp=0, weakness=None, type=None, secondary=None,*extra_moves):
        super().__init__(name, hp, weakness, type)
        self.secondary = secondary
        self.extra_moves = extra_moves

        self.move_lst = list(self.extra_moves)
        self.var1 = []
        self.var2 = ""
        for i in self.extra_moves:
            self.var1 = list(i)
        self.var2 += ", ".join(self.var1)

    def get_type(self):
        if self.secondary == None:
            return f"Main type: {self.type}"
        else:
            return f"Main type: {self.type} Secondary type: {self.secondary}"

    def get_move(self):
        if len(self.extra_moves) == 0:
            return "Basic move: Quick Attack"
        else:
            return f"Basic move: Quick Attack\nOther moves: {str(self.var2)}"

print("\n------------Basic Info:--------------")
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print("\n------------Pokemon 1 Info:-------------")
charmander = PokemonExtra("Charmander", 39, "Water", "Fire")
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print("\n------------Pokemon 2 Info:-------------")
charizard = PokemonExtra(
    "Charizard", 78, "Water", "Fire", "Flying", ("Fire Spin", "Fire Blaze")
)
print(charizard)
print(charizard.get_type())
print(charizard.get_move())

# Task 08

class Team:
    def __init__(self, name):
        self.name = "default"
        self.total_player = 5

    def info(self):
        print("We love sports")

class FootBallTeam(Team):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.total_player = 11

    def info(self):
        print(f"Our name is {self.name}\nWe play Football")
        super().info()

class CricketTeam(Team):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.total_player = 11

    def info(self):
        print(f"Our name is {self.name}\nWe play Cricket")
        super().info()

class Team_test:
    def check(self, tm):
        print("=========================")
        print("Total Player:", tm.total_player)
        tm.info()

f = FootBallTeam("Brazil")
c = CricketTeam("Bangladesh")
test = Team_test()
test.check(f)
test.check(c)

# Task 09

class Pokemon:
    def __init__(self, p):
        self.pokemon = p
        self.pokemon_type = "Needs to be set"
        self.pokemon_weakness = "Needs to be set"

    def kind(self):
        return self.pokemon_type

    def weakness(self):
        return self.pokemon_weakness

    def what_am_i(self):
        print("I am a Pokemon.")

class Pikachu(Pokemon):
    def __init__(self, name="Pikachu", type="Electric", weakness="Ground"):
        super().__init__(name)
        self.pokemon_type = type
        self.pokemon_weakness = weakness

    def what_am_i(self):
        super().what_am_i()
        print(f"I am {self.pokemon}")

class Charmander(Pokemon):
    def __init__(self, name="Charmander", type="Fire", weakness="Water, Ground and Rock"):
        super().__init__(name)
        self.pokemon_type = type
        self.pokemon_weakness = weakness

    def what_am_i(self):
        super().what_am_i()
        print(f"I am {self.pokemon}")

pk1 = Pikachu()
print("Pokemon:", pk1.pokemon)
print("Type:", pk1.kind())
print("Weakness:", pk1.weakness())
pk1.what_am_i()
print("========================")
c1 = Charmander()
print("Pokemon:", c1.pokemon)
print("Type:", c1.kind())
print("Weakness:", c1.weakness())
c1.what_am_i()

# Task 10

class Department:
    def __init__(self, s):
        self.semester = s
        self.name = "Default"
        self.id = -1

    def student_info(self):
        print("Name:", self.name)
        print("ID:", self.id)

    def courses(self, c1, c2, c3):
        print("No courses Approved yet!")

class CSE(Department):
    def __init__(self, name, ID, semester):
        super().__init__(semester)
        self.name = name
        self.id = ID

    def student_info(self):
        super().student_info()
        print(f"Courses Approved to this CSE student in {self.semester} semester: ")

    def courses(self, c1, c2, c3):
        print(f"{c1}\n{c2}\n{c3}")

class EEE(Department):
    def __init__(self, name, ID, semester):
        super().__init__(semester)
        self.name = name
        self.id = ID

    def student_info(self):
        super().student_info()
        print(f"Courses Approved to this EEE student in {self.semester} semester: ")

    def courses(self, c1, c2, c3):
        print(f"{c1}\n{c2}\n{c3}")

s1 = CSE("Rahim", 16101328, "Spring2016")
s1.student_info()
s1.courses("CSE110", "MAT110", "ENG101")
print("==================")
s2 = EEE("Tanzim", 18101326, "Spring2018")
s2.student_info()
s2.courses("Mat110", "PHY111", "ENG101")
print("==================")
s3 = CSE("Rudana", 18101326, "Fall2017")
s3.student_info()
s3.courses("CSE111", "PHY101", "MAT120")
print("==================")
s4 = EEE("Zainab", 19201623, "Summer2019")
s4.student_info()
s4.courses("EEE201", "PHY112", "MAT120")

# Task 11 (Tracing)

class A:
    def __init__(self):
        self.temp = 4
        self.sum = 1
        self.y = 2
        self.y = self.temp - 2
        self.sum = self.temp + 3
        self.temp -= 2
    def methodA(self, m,  n):
        x = 0
        self.y = self.y + m + self.temp
        self.temp += 1
        x = x + 2 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)

class B(A):
    def __init__(self, b=None):
        super().__init__()
        self.x = 1
        self.sum = 2
        if b == None:
            self.y = self.temp + 3
            self.sum = 3 + self.temp + 2
            self.temp -= 1
        else:
            self.sum = b.sum
            self.x = b.x
    def methodB(self, m,  n):
        y = 0
        y = y + self.y
        self.x = y + 2 + self.temp
        self.methodA(self.x, y)
        self.sum = self.x + y + self.sum
        print(self.x, y, self.sum)

a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(1, 1)
b1.methodA(1, 2)
b2.methodB(3, 2)

# Task 12   (Tracing)

class A:
    temp = 4
    def __init__(self):
        self.sum = 0
        self.y = 0
        self.y = A.temp - 2
        self.sum = A.temp + 1
        A.temp -= 2
    def methodA(self, m,  n):
        x = 0
        self.y = self.y + m + (A.temp)
        A.temp += 1
        x = x + 1 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)

class B(A):
    x = 0
    def __init__(self,b=None):
        super().__init__()
        self.sum = 0
        if b==None:
            self.y = A.temp + 3
            self.sum = 3 + A.temp + 2
            A.temp -= 2
        else:
            self.sum = b.sum
            B.x = b.x
            b.methodB(2, 3)
    def methodB(self, m,  n):
        y = 0
        y = y + self.y
        B.x = self.y + 2 + A.temp
        self.methodA(B.x, y)
        self.sum = B.x + y + self.sum
        print(B.x, y, self.sum)

a1 = A()
b1 = B()
b2 = B(b1)
b1.methodA(1, 2)
b2.methodB(3, 2)

# Task 13   (Tracing)

class A:
  temp = 3
  def __init__(self):
    self.sum = 0
    self.y = 0
    self.y = A.temp - 1
    self.sum = A.temp + 2
    A.temp -= 2

  def methodA(self, m, n):
    x = 0
    n[0] += 1
    self.y = self.y + m + A.temp
    A.temp += 1
    x = x + 2 + n[0]
    n[0] = self.sum + 2
    print(f"{x} {self.y} {self.sum}")

class B(A):
  x = 1
  def __init__(self, b = None):
    super().__init__()
    self.sum = 2
    if b == None:
      self.y = self.temp + 1
      B.x = 3 + A.temp + self.x
      A.temp -= 2
    else:
      self.sum = self.sum + self.sum
      B.x = b.x + self.x
  def methodB(self, m, n):
    y = [0]
    self.y = y[0] + self.y + m
    B.x = self.y + 2 +  self.temp - n
    self.methodA(self.x, y)
    self.sum = self.x + y[0] + self.sum
    print(f"{self.x} {y[0]} {self.sum}")

x = [23]
a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(1, x)
b2.methodB(3, 2)
a1.methodA(1, x)

# Task 14    (Tracing)

class A:
  temp = 7
  def __init__(self):
    self.sum, self.y = 0, 0
    self.y = A.temp - 1
    self.sum = A.temp + 2
    A.temp -= 3
  def methodA(self, m, n):
    x = 4
    n[0] += 1
    self.y = self.y + m + A.temp
    A.temp += 2
    x = x + 3 + n[0]
    n[0] = self.sum + 2
    print(f"{x} {self.y} {self.sum}")
  def get_A_sum(self):
    return self.sum
  def update_A_y(self, val):
    self.y = val
class B(A):
  x = 2
  def __init__(self, b = None):
    super().__init__()
    self.sum = 2
    if b == None:
      self.y = self.temp + 1
      B.x = 4 + A.temp + self.x
      A.temp -= 2
    else:
      self.sum = self.sum + self.get_A_sum()
      B.x = b.x + self.x
  def methodB(self, m, n):
    y = [0]
    self.update_A_y(y[0] + self.y + m)
    B.x = self.y + 4 +  self.temp - n
    self.methodA(self.x, y)
    self.sum = self.x + y[0] + self.get_A_sum()
    print(f"{self.x} {y[0]} {self.sum}")

x = [32]
a1 = A()
b1 = B()
b2 = B(b1)
a1.methodA(2, x)
b2.methodB(2, 3)
a1.methodA(3, x)
