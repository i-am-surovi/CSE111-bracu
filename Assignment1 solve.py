## Task 1
def BMI(height,weight):

  bmi = round(weight/(height**2),1)

  if bmi < 18.5:
    condition = "Underweight"
    print("Score is {}. You are {}".format(bmi,condition))

  elif 18.5 <= bmi <= 24.9:
    condition = "Normal"
    print("Score is {}. You are {}".format(bmi,condition))

  elif 25 <= bmi <= 30:
    condition = "Overweight"
    print("Score is {}. You are {}".format(bmi,condition))

  elif 30 < bmi:
    condition = "Obese"
    print("Score is {}. You are {}".format(bmi,condition))

height = int(input("Enter your height in cm: "))/100
weight = int(input("Enter your weight in kg: "))

BMI(height,weight)


## Task 2
def number(minimum,maximum,divisor):
  count = minimum
  sum = 0
  while count < maximum:
    if count % divisor == 0:
      sum += count
    count += 1
  return(sum)

minimum = int(input())
maximum = int(input())
divisor = int(input())

number(minimum,maximum,divisor)


## TAsk 3
menu = {'BBQ Chicken Cheese Burger':250,'Beef Burger':170,'Naga Drums':200}

def total_price(items_name,location):
  meal_cost = 0
  delivery_charge = 0

  for i in items_name:
    for k,v in menu.items():
      if i==k:
        meal_cost += v
      else:
        continue

  if location == "Mohakhali":
    delivery_charge += 40
  else:
    delivery_charge += 60

  tax = round(meal_cost*(8/100),1)
  total_cost = meal_cost + delivery_charge + tax

  print(total_cost)

items_name = input("Enter items name separated by comma: ").split(', ')

location = input("Enter your location: ")

total_price(items_name,location)


## TAsk 4
def replace_domain(email, new_domain, old_domain = 'kaaj.com'):

    check = email.find('@')

    if email[check+1:] == old_domain:
        new_email = email[:check+1] + new_domain
        print("Changed: ",new_email)

    else:
        print("Unchanged: ",email)

email = input("Enter your email: ")
new_domain = input("Enter the new domain: ")

replace_domain(email, new_domain, old_domain = 'kaaj.com')


## Task 5
def palindrome(given_string):

  if " " in given_string:
    given_string = given_string.replace(" ","")

    if given_string == given_string[: :-1]:
      print("Palindrome")
    else:
      print("Not Palindrome")

  else:
    if given_string == given_string[: :-1]:
      print("Palindrome")
    else:
      print("Not Palindrome")

given_string = input("Enter string here: ")

palindrome(given_string)


## Task 6
def capitalize(paragraph):

    correct_paragraph = ""

    full_stop = 0
    exclamation_mark = 0
    question_mark = 0

    correct_paragraph += paragraph[0].upper()

    for i in range(1,len(paragraph)):

        if paragraph[i].isalpha() == False:
            correct_paragraph += paragraph[i]

        elif paragraph[i] == 'i' and paragraph[i-1].isalpha() == False and paragraph[i+1].isalpha() == False:
            correct_paragraph += paragraph[i].upper()

        elif full_stop == 1:
            correct_paragraph += paragraph[i].upper()
            full_stop = 0

        elif exclamation_mark == 1:
            correct_paragraph += paragraph[i].upper()
            exclamation_mark = 0

        elif question_mark == 1:
            correct_paragraph += paragraph[i].upper()
            question_mark = 0

        else:
            correct_paragraph += paragraph[i]


        if paragraph[i] == '.':
            full_stop = 1

        elif paragraph[i] == '!':
            exclamation_mark = 1

        elif paragraph[i] == '?':
            question_mark = 1

    return correct_paragraph


paragraph = input("Enter the paragraph: ")
capitalize(paragraph)

correct_paragraph = capitalize(paragraph)
print(correct_paragraph)
