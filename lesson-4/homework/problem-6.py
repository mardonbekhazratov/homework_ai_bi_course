tubs = []
for i in range(2,1001):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        tubs.append(i)

print(*tubs)