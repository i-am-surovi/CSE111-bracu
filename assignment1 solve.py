## Task 1
given_string = "HOusE"
upper_case = 0
lower_case = 0

for i in given_string:
  if 65<=ord(i)<=90:
    upper_case += 1
  elif 97<=ord(i)<=122:
    lower_case += 1

if upper_case > lower_case:
    print(given_string.upper())
else:
    print(given_string.lower())


## Task 2
given_string = "jhg231j213"
word_count = 0
number_count = 0

for i in given_string:
  if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:

    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
      word_count += 1
    elif 48 <= ord(i) <= 57:
      number_count += 1

if word_count > 0 and number_count > 0:
  print("MIXED")

elif word_count > 0:
  print("WORD")

elif number_count > 0:
  print("NUMBER")


## Task 3
n = "coDIng" / n = "baNgladEsh"
c = ""
for i in n:
  if 65 <= ord(i) <= 90:
    c += i
    
s = n.index(c[0]) + 1
e = n.index(c[1])
between = n[s:e]

if between != "":
  print(between)
else:
  print("BLANK")


## Task 4
given_string_1 = "harry"
given_string_2 = "hermione"

set_1 = set(given_string_1)
set_2 = set(given_string_2)

created_string = ""
for i in given_string_1:
  if i in set_2:
    created_string += i

for j in given_string_2:
  if j in set_1:
    created_string += j

if created_string == "":
  print("Nothing in common")
else:
  print(created_string)


## Task 5
new_password = input("Please enter your new password: ")

lower_count = 0
upper_count = 0
digit_count = 0
special_count = 0

for i in new_password:
  if 48 <= ord(i) <= 57:
    digit_count += 1
  elif 65 <= ord(i) <= 90:
    upper_count += 1
  elif 97 <= ord(i) <= 122:
    lower_count += 1
  else:
    special_count += 1

missing = []

if lower_count == 0:
  missing.append("Lowercase character missing")
elif upper_count == 0:
  missing.append("Uppercase character missing")
elif digit_count == 0:
  missing.append("Digit missing")
elif special_count == 0:
  missing.append("Special character missing")
else:
  missing.append("OK")

print(*missing, sep= ', ')
