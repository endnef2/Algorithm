m, d = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = [ 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = 0
if m > 1:
    for i in range(1, m):
        day = day + month[i-1]
else:
    pass
print(week[(day + d)%7])