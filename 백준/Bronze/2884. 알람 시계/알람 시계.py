a, b = map(int, input().split())
if a >= 1 and b < 45 :
    print(a-1 , (b+60)-45)
elif a < 1 and b < 45 :
    print(23 , (b+60)-45)
else :
    print(a , b-45)