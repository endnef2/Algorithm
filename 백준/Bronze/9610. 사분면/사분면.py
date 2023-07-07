num = int(input())
lst1 = [0]*5
for _ in range(num):
    a, b = map(int, input().split())
    if a==0 or b==0:
        lst1[4]+=1
    elif a > 0:
        if b > 0:
            lst1[0]+=1
        else:
            lst1[3]+=1
    else:
        if b > 0:
            lst1[1]+=1            
        else:
            lst1[2]+=1
print(f"Q1: {lst1[0]}\nQ2: {lst1[1]}\nQ3: {lst1[2]}\nQ4: {lst1[3]}\nAXIS: {lst1[4]}")