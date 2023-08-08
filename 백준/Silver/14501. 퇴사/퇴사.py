N = int(input())
consult = []
for i in range(N):
    T, P = map(int, input().split())
    consult.append((T, P))

stack = [(0, 0)]
max_p = 0
while len(stack)>0:
    date, profit = stack.pop()
    # N보다 큰 경우 다음으로...
    if date > N:
        continue
    # 현재 date 상담 불가능하면 다음 날짜로
    if date+1 <=N:
        stack.append((date+1, profit))

    # 현재 date 상담 가능
    if date <N and date+consult[date][0] <= N:
        next_date = date+consult[date][0]
        next_profit = profit+consult[date][1] 
        stack.append((next_date, next_profit))
        # max 값보다 크면 값 바꾸기
        if max_p < next_profit:
            max_p = next_profit
print(max_p)