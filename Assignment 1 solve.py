# Task 1
f = input("Enter a dictionary: ")
s = input("Enter another dictionary: ")
l1 = f.split(",")
l2 = s.split(",")
d1 = {}
d2 = {}

for i in l1:
  kv = i.split(":")
  d1[kv[0]] = int(kv[1])

for j in l2:
  kv = j.split(":")
  d2[kv[0]] = int(kv[1])

d = {}

for k,v in d1.items():
  if k in d2:
    d[k] = d1[k] + d2[k]
  else:
    d[k] = v

for k,v in d2.items():
  if k in d1:
    d[k] = d1[k] + d2[k]
  else:
    d[k] = v

print(d)

l3 = []
for k,v in d.items():
  if v not in l3:
    l3.append(v)
t = tuple(sorted(l3))
print("Values:",t)

# Task 2
user_input = input()
list_1 = []

while user_input != "STOP":
  list_1.append(user_input)
  user_input = input()

dictionary = {}
for i in list_1:
  if i in dictionary:
    dictionary[i] += 1
  else:
    dictionary[i] = 1

for i,j in dictionary.items():
  n = i
  f = j
  print(f"{n} - {f} times")

# Task 3
d1 = {'key1':'value1','key2':'value2','key3':'value1'}
d2 = {}

for k,v in d1.items():
  if v in d2:
    d2[v].append(k)
  else:
    d2[v] = [k]

print(d2)

# Task 4
key_presses = {'1':['.',',','?','!',':'],'2':[['A','a'],['B','b'],['C','c']],'3':[['D','d'],['E','e'],['F','f']],'4':[['G','g'],['H','h'],['I','i']],'5':[['J','j'],['K','k'],['L','l']],'6':[['M','m'],['N','n'],['O','o']],'7':[['P','p'],['Q','q'],['R','r'],['S','s']],'8':[['T','t'],['U','u'],['V','v']],'9':[['W','w'],['X','x'],['Y','y'],['Z','z']],'0':[' ']}

text = list(input("Please write a message: "))

for i in text:
  for k,v in key_presses.items():
    for j in v:
      if i in j:
        n = v.index(j)

        print(k*(n+1),end="")
