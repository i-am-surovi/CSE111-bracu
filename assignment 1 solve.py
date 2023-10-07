## Task 1
l1 = []
l2 = []
inp=''
while inp != 'STOP':
  inp = input()
  if inp != 'STOP':
    l1.append(inp)

for i in l1:
  if i not in l2:
    l2.append(i)

for i in range(len(l2)):
  print(l2[i], '-', l1.count(l2[i]),'times')


## Task 2
n=int(input())
l1=[]
l2=[]
for j in range(n):
  a=[int(i) for i in input().split(' ')]
  sum = 0
  for i in a:
    sum = sum + i
  l1.append(a)
  l2.append(sum)

b=(max(l2))
for i in range(0,len(l2)):
  if l2[i]==b:
    print(b)
    print(l1[i])


## Task 3
b = ''
f = False
while b != 'STOP':
  b = str(input())
  if b != 'STOP':
    a = [int(i) for i in b.split(' ')]
    for i in range(0,len(a)-1):
      if abs(a[i]-a[i+1]) < (len(a)) :
        f = True
      else:
        f = False
        break
    if f == True:
      print('UB jumper')
    else:
      print('Not UB jumper')
  else:
    break


## Task 4
n,k = input().split ()
members = input().split()
eligible_members = 0

for i in members:
    if int(i) + int(k) <= 5:
        eligible_members += 1
print(eligible_members // 3)

