L, C = map(int,input().split())
code_list = sorted(list(input().split()))
ret_list = [0]*L
vowel = ['a', 'e', 'i', 'o', 'u']
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
consonant = set(alphabet_list)-set(vowel)
def dfs(depth, idx):
    if depth == L:
        vol_cnt=0
        con_cnt=0
        for i in ret_list:
            if i in vowel:
                vol_cnt+=1
            if i in consonant:
                con_cnt+=1
        if vol_cnt >=1 and con_cnt>=2 :
            print(*ret_list, sep='')
    else:
        for jdx in range(idx, C):
            ret_list[depth] = code_list[jdx]
            dfs(depth+1, jdx+1)
dfs(0,0)