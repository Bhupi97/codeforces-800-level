n = int(input())
ans = 0
for _ in range(n):
    ops = input()
    if ops.find('++')>-1:
        ans += 1
    else:
        ans -= 1

print(ans)
