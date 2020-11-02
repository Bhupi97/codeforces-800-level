w = int(input())
for _ in range(w):
    s = input()
    if len(s) < 11:
        print(s)
    else:
        ss = "{}{}{}".format(s[0],(len(s)-2),s[-1])
        print(ss)
        
    
