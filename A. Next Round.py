n, s = input().split()
n, s = int(n), int(s)
testScores = list(map(int,input().split()))
ans = 0
for i in range(n):
    if testScores[i] >= testScores[s-1] and testScores[i]>0:
        ans += 1


print(ans)
    
