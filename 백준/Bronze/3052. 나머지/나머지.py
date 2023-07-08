total = []
for _ in range(10):
     num = (int(input())) % 42
     total.append(num)
print(len(set(total)))