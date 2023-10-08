# Task 1
class Patient:
  def __init__(self, name, age, weight, height):
    self.name = name
    self.age = age
    self.weight = weight
    self.height = height/100

    BMI = self.weight/(self.height**2)
    self.bmi = BMI

  def printDetails(self):
    print("Name:",self.name)
    print("Age:",self.age)
    print("Weight:",self.weight,"kg")
    print("Height:",self.height,"cm")
    print("BMI:",self.bmi)

p1 = Patient("A", 55, 63.0, 158.0)
p1.printDetails()
print("====================")
p2 = Patient("B", 53, 61.0, 149.0)
p2.printDetails()

# Task 2
class Shape:

  def __init__(self, shape, height, sides):
    self.shape = shape
    self.height = height
    self.sides = sides

  def area(self):

    if self.shape == "Triangle" or self.shape == "Rhombus":
      area = 0.5 * self.height * self.sides
      print("Area:",area)

    elif self.shape == "Square" or self.shape == "Rectangle":
      area = self.height * self.sides
      print("Area:",area)

    else:
      print("Area: Shape unknown")


triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()

# Task 3
class Calculator:
  def __init__(self):
    print("Calculator is ready")

  def calculate(self, v1, v2, sign):
    self.v1 = v1
    self.v2 = v2
    self.sign = sign

    if sign == "+":
      self.answer = self.v1 + self.v2
      return self.answer

    elif sign == "-":
      self.answer = self.v1 - self.v2
      return self.answer

    elif sign == "*":
      self.answer = self.v1 * self.v2
      return self.answer

    elif sign == "/":
      self.answer = self.v1 / self.v2
      return self.answer

    else:
      return "Wrong Input"

  def showCalculation(self):
    print(f"{self.v1} {self.sign} {self.v2} = {self.answer}")

c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()

# Task 4
class Programmer:
  def __init__(self, name, language, exp):
        self.name = name
        self.language = language
        self.exp = exp
        print("Horray! A new programmer is born")

  def addExp(self, additional_exp):
        print(f"Updating experience of {self.name}")
        self.exp += additional_exp

  def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Language: {self.language}")
        print(f"Experience: {self.exp} years")


p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print("--------------------------")
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print("--------------------------")
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()

# Task 5
class  UberEats:
  def __init__(self, name, phone, address):
    self.name = name
    self.phone = phone
    self.address = address
    self.food = {}

    print(f'{self.name}, welcome to UberEats!')

  def add_items(self, items_1, items_2, p1, p2):
    self.food[items_1] = p1
    self.food[items_2] = p2
    self.items_1 = items_1
    self.items_2 = items_2
    self.p1 = p1
    self.p2 = p2

  def print_order_detail(self):
    return f"User details: Name: {self.name}, Phone: {self.phone}, Address: {self.address} \nOrders: {self.food} \nTotal Paid Amount: {self.p1+self.p2}"

order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())

# Task 6
class Customer:
    def __init__(self, name):
        self.name = name

    def greet(self, name=None):
        if name != None:
            print(f"Hello {name}!")
        else:
            print("Hello!")

    def purchase(self, *item):
        print(f"{self.name}, you purchased {len(item)} items(s):")
        for i in item:
            print(i)

customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")

# Task 7
## Task 7

class Cat:
    def __init__(self, color="White", activity="sitting"):
        self.color = color
        self.activity = activity

    def printCat(self):
        print(f"{self.color} cat is {self.activity}")

    def changeColor(self, new_color):
        self.color = new_color

c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()

# Task 8
## Task 8

class Student:
    def __init__(self, name, ID, dept="CSE"):
        self.name = name
        self.ID = ID
        self.dept = dept

    def dailyEffort(self, hours):
        self.hours = hours

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.ID}")
        print(f"Department: {self.dept}")
        print(f"Daily Effort: {self.hours} hour(s)")

        if self.hours <= 2:
            print("Suggestion: Should give more effort!")
        elif self.hours <= 4:
            print("Suggestion: Keep up the good work!")
        else:
            print("Suggestion: Execellent! Now motivate others.")

harry = Student("Harry Potter", 123)
harry.dailyEffort(3)
harry.printDetails()
print("========================")
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print("========================")
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()

# Task 9
## Task 9

class Batsman:
    def __init__(self, *var):
        if len(var) == 2:
            runs, balls = var
        else:
            player, runs, balls = var

        if len(var) != 2:
            self.name = player
        else:
            self.name = "New Batsman"

        self.runs = runs
        self.balls = balls

    def setName(self, name):
        self.name = name

    def battingStrikeRate(self):
        return (self.runs) / (self.balls) * 100

    def printCareerStatistics(self):
        print(f"Name: {self.name}")
        print(f"Runs Scored: {self.runs}, Balls Faced: {self.balls}")


b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())

# Task 10
## Task 10

class Author:
    def __init__(self, name=None, *books):
        self.name = name
        if name == None:
            self.name = "Default"

        booklist = ""
        if len(books) > 0:
            for i in books:
                booklist += i + "\n"
            self.books = booklist

    def changeName(self, new_name):
        self.name = new_name

    def addBooks(self, *books):
        booklist = ""
        for i in books:
            booklist += i + "\n"

        self.books = booklist

    def printDetails(self):
        print(f"Author Name: {self.name}")
        print("------------")
        print("List of Books:")
        print(self.books)

auth1 = Author("Humayun Ahmed")
auth1.addBooks("Deyal", "Megher Opor Bari")
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName("Mario Puzo")
auth2.addBooks("The Godfather", "Omerta", "The Sicilian")
print("===================")
auth2.printDetails()
print("===================")
auth3 = Author("Paolo Coelho", "The Alchemist", "The Fifth Mountain")
auth3.printDetails()

# Task 11
## Task 11

class TaxiLagbe:
  def __init__(self, taxi_number,location):
    self.taxi_number = taxi_number
    self.location = location
    self.fair = 0
    self.passengers = []

  def addPassenger(self, *arg):
    if len(self.passengers) == 4:
      print("Taxi Full! No more passengers can be added.")
      return
    for i in arg:
      name, fair = i.split("_")
      self.fair+=int(fair)
      self.passengers.append(name)

      print(f"Dear {name}! Welcome to TaxiLagbe. ")

  def printDetails(self):
    print("Trip info for Taxi number:",self.taxi_number)
    print("This taxi can cover only",self.location,"area.")
    print("Total passengers:",len(self.passengers))
    print("Passenger lists: ")
    # Passenger lists:
    print(*self.passengers, sep=", ")
    print("Total collected fare:",self.fair,"Taka")

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()

# Task 12
## Task 12

class Account():

  def __init__(self, name = "Default Account", balance = 0.0):
    self.name = name
    self.balance = balance

  def details(self):
    return f"{self.name}\n{self.balance}"

  def withdraw(self, amount):
    if self.balance - amount <= 3070:
      print("Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.")
    else:
      self.balance -= amount
      print("Withdraw successful! New balance is: ",self.balance)

a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)

# Task 13
## Task 13

class StudentDatabase:

  def __init__(self, name, id):
    self.name = name
    self.id = id
    self.grades = {}

  def calculateGPA(self, courses, intake):
    self.intake = intake
    self.credits_grades = []
    self.courses = []
    self.grade = []

    for i in courses:
      self.credits_grades.append(i.split(":"))
    for j in self.credits_grades:
      self.courses.append(j[0])
      self.grade.append(j[1])

    self.grade = [float(i) for i in self.grade]
    sum = 0
    gpa = 0

    for i in self.grade:
      sum = sum + (i*3)
      gpa = round(sum/(3*len(self.courses)),2)

    self.grades[self.intake] = {tuple(self.courses):gpa}

  def printDetails(self):
    print(f'Name: {self.name}')
    print(f'ID: {self.id}')

    for i in self.grades:                 # this wil traverse through all the keys
        print(f'Courses taken in {i}:')   # all the keys of this dict are Semester's name
        x_dict = self.grades[i]           # this is the small dict "{('CSE230', 'CSE220', 'MAT110'): 4.0}"

        for j in x_dict:                  # we will traverse the small dict
            print(*j, sep = '\n')         # j will be the key of the small dict which is a tuple and we can print the values of tuple in this way or u could have used another loop
            print(f'GPA: {x_dict[j]}')    # the keys corresponding value is the gpa

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()

# Task 14  (Tracing)
class Test3:

    def __init__(self):
        self.sum, self.y = 0, 0

    def methodA(self):
        x, y = 2, 3
        msg = [0]
        msg[0] = 3
        y = self.y + msg[0]
        self.methodB(msg, msg[0])
        x = self.y + msg[0]
        self.sum = x + y + msg[0]
        print(x, y, self.sum)

    def methodB(self, mg2, mg1):
        x = 0
        self.y = self.y + mg2[0]
        x = x + 33 + mg1
        self.sum = self.sum + x + self.y
        mg2[0] = self.y + mg1
        mg1 = mg1 + x + 2
        print(x, self.y, self.sum)

t3 = Test3()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()

# Task 15  (Tracing)
class Test5:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x = 0
        z = 0
        while (z < 5):
            self.y = self.y + self.sum
            x = self.y + 1
            print(x, self.y, self.sum)
            self.sum = self.sum + self.methodB(x, self.y)
            z += 1
    def methodB(self, m, n):
        x = 0
        sum = 0
        self.y = self.y + m
        x = n - 4
        sum = sum + self.y
        print(x, self.y, sum)
        return self.sum

t5 = Test5()
t5.methodA()

# Task 16  (Tracing)
class FinalT6A:
    def __init__(self, x, p):
        self.temp, self.sum, self.y = 4, 0, 1
        self.temp += 1
        self.y = self.temp - p
        self.sum = self.temp + x
        print(x, self.y, self.sum)
    def methodA(self):
        x = 0
        y = 0
        y = y + self.y
        x = self.y + 2 + self.temp
        self.sum = x + y + self.methodB(self.temp, y)
        print(x, y, self.sum)
    def methodB(self, temp, n):
        x = 0
        temp += 1
        self.y = self.y + temp
        x = x + 3 + n
        self.sum = self.sum + x + self.y
        print(x, self.y, self.sum)
        return self.sum

q1 = FinalT6A(2,1)
q1.methodA()
q1.methodA()

# Task 17  (Tracing)
class Test5:
  def __init__(self):
      self.sum = 0
      self.y = 0
  def methodA(self):
      x=y=k=0
      msg = [5]
      while (k < 2):
          y += msg[0]
          x = y + self.methodB(msg, k)
          self.sum = x + y + msg[0]
          print(x ," " , y, " " , self.sum)
          k+=1
  def methodB(self, mg2, mg1):
        x = 0
        self.y += mg2[0]
        x = x + 3 + mg1
        self.sum += x + self.y
        mg2[0] = self.y + mg1
        mg1 += x + 2
        print(x , " " ,self.y, " " , self.sum)
        return mg1

t1 = Test5()
t1.methodA()
t1.methodA()
t1.methodA()

# Task 18  (Tracing)
class Test4:
    def __init__(self):
        self.sum, self.y = 0, 0
    def methodA(self):
        x, y = 0, 0
        msg = [0]
        msg[0] = 5
        y = y + self.methodB(msg[0])
        x = y + self.methodB(msg, msg[0])
        self.sum = x + y + msg[0]
        print(x, y, self.sum)
    def methodB(self, *args):
        if len(args) == 1:
            mg1 = args[0]
            x, y = 0, 0
            y = y + mg1
            x = x + 33 + mg1
            self.sum = self.sum + x + y
            self.y = mg1 + x + 2
            print(x, y, self.sum)
            return y
        else:
            mg2, mg1 = args
            x = 0
            self.y = self.y + mg2[0]
            x = x + 33 + mg1
            self.sum = self.sum + x + self.y
            mg2[0] = self.y + mg1
            mg1 = mg1 + x + 2
            print(x, self.y, self.sum)
            return self.sum

t3 = Test4()
t3.methodA()
t3.methodA()
t3.methodA()
t3.methodA()

# Task 19  (Tracing)
class msgClass:
    def __init__(self):
        self.content = 0
class Q5:
    def __init__(self):
        self.sum = 1
        self.x = 2
        self.y = 3
    def methodA(self):
        x, y = 1, 1
        msg = []
        myMsg = msgClass()
        myMsg.content = self.x
        msg.append(myMsg)
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])##
        y = self.methodB(msg[0]) + self.y
        x = y + self.methodB(msg[0], msg)
        self.sum = x + y + msg[0].content
        print(x," ", y," ", self.sum)
    def methodB(self, mg1, mg2 = None):
        if mg2 == None:
            x, y = 5, 6
            y = self.sum + mg1.content
            self.y = y + mg1.content
            x = self.x + 7 +mg1.content
            self.sum = self.sum + x + y
            self.x = mg1.content + x +8
            print(x, " ", y," ", self.sum)
            return y
        else:
            x = 1
            self.y += mg2[0].content
            mg2[0].content = self.y + mg1.content
            x = x + 4 + mg1.content
            self.sum += x + self.y
            mg1.content = self.sum - mg2[0].content
            print(self.x, " ",self.y," ", self.sum)
            return self.sum

q = Q5()
q.methodA()





