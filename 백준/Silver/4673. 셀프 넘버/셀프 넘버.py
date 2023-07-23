num = set(range(0, 10001))
gen_num = set()
for i in range(0, 10001):
    for j in str(i):
        i = i+int(j)
    gen_num.add(i)
print(*sorted(num-gen_num), sep='\n')