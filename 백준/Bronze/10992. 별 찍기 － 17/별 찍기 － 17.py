num = int(input())
for i in range(1, num):
    if i>1:
        print(' '*(num-i)+'*'+' '*(2*(i-1)-1)+ '*')
    else:
        print(' '*(num-i)+'* '*(i))
print('*'*((num-1)*2+1))