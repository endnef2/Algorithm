N, M = map(int, input().split())
chess = []
for i in range(N):
    row = input()
    chess.append(row)
min_count = 5000
for i in range(N-7):
    for j in range(M-7):
        w_cnt = 0 # 첫번째 W경우
        b_cnt = 0 # 첫번째 B경우
        for k in range(i, i+8):
            for l in range(j, j+8):
                string = chess[k][l]
                if (k+l)%2 == 0: # 두 인덱스 더한 값이 2의 배수
                    if string != 'W':
                        w_cnt+=1
                    if string != 'B':
                        b_cnt+=1
                else: # 두 인덱스 더한 값 2의 배수 아님
                    if string != 'W':
                        b_cnt+=1
                    if string != 'B':
                        w_cnt+=1
        min_count = min(min_count, w_cnt, b_cnt)
print(min_count)