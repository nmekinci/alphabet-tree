import string
e = int(input("enter: "))
alp = list(string.ascii_uppercase)
if e**2 > len(alp):
  for i in range((e**2 // 26) + 1):
    alp.extend(string.ascii_uppercase)
c = 0
for i in range(1,e+1):
  for j in alp[c:c+i]:
    print(j,end=' ')
  print('')
  c += i

for i in range(e+1,0,-1):
  for j in alp[c:c+i]:
    print(j,end=' ')
  print('')
  c += i