def dEndedStr(s1, s2, c):
    ls1 = len(s1)
    ls2 = len(s2)
    if s1 == s2:
        return c
    if s1[0]!= s2[0]:
        if ls1 > ls2:
            dEndedStr(s1[1:], s2, c+1)
        else:
            dEndedStr(s1, s2[1:], c+1)
    if s1[ls1-1]!= s2[ls2-1]:
        if ls1 > ls2:
            dEndedStr(s1[0:ls1-2], s2, c+1)
        else:
            dEndedStr(s1, s2[0:ls2-2], c+1)
        
            


n = int(input())

for _ in range(n):
    c = 0
    s1 = input()
    s2 = input()
    print(dEndedStr(s1, s2, c))
    
    
