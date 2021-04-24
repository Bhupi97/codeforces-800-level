def getSorted(s):
    if len(s)<2:
        return s

    s = s.split('+')
    #print(s)
    a1 = sorted(s)
    #print(a1)
    a2 = '+'.join(a1)
    return a2


s = input()

print(getSorted(s))
