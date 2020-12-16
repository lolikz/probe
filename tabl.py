a = 7
b = 10
c = 5
d = 6

for i in range(c, d + 1):
    print('\t', i, end=' ')
print()
for j in range(a, b + 1):
    print(j, end=' ')
    for i in range(c, d + 1):
        print('\t', j * i, end=' ')
    print()
