N, B = map(int, input().split())
lst1 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
while N:
    result+=str(lst1[N%B])
    N = N//B
print(result[::-1], sep='')