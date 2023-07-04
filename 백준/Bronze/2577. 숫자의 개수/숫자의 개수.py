a = int(input())
b = int(input())
c = int(input())
num = list(str(a*b*c))
answer = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in num:
    answer[int(i)]=num.count(i)
for i in answer:
    print(i)