multi = []

for i in range(900,1000):
    for j in range(900,1000):
        k=str(i*j)
        if k == k[::-1]:
            multi.append(k)

print(multi)
