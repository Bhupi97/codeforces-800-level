def ans(p):
 if p**(1/2) == int(p**(1/2)):
  return 'NO'
 return 'YES'
 
t = int(input())

for _ in range(t):
 n = int(input())
 l = input().split()
 p = 1
 for i in range(n):
  p *= int(l[i])
 print(ans(p))
 