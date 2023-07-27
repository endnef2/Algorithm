n = int(input())
cnt = 0
while cnt<n:
        print("* "*(n-1)+'*')
        cnt+=1
        if cnt==n:
                break
        print("","* "*(n-1)+'*')
        cnt+=1