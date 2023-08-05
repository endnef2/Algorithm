ret_list = [0,0,0,0,0,0]
def Fn(depth, idx):
    if depth == 6:
        print(*ret_list)
        return
    for jdx in range(idx, N):
        ret_list[depth] = lotto_list[jdx]
        Fn(depth+1, jdx+1)
        
while True :
    lst1 = list(map(int, input().split()))
    if lst1 == [0] :
        break
    N = lst1[0]
    lotto_list = lst1[1:]
    Fn(0, 0)
    print('')