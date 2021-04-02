a,b = input().split(" ")
aR = int(a[::-1])
bR = int(b[::-1])

if aR > bR :
    print(aR)
else :
    print(bR)