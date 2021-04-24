def sumOfdigits(n):
 return 0 if n == 0 else int(n%10) + sumOfdigits(int(n/10))
t = int(input())
for _ in range(t):
 n = int(input())
 if n%2050 != 0:
  print(-1)
 else:
  print(sumOfdigits(n/2050))
