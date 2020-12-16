a = int(input())
b = int(input())
c = int(input())

if c <= a >= b:
    max = a
elif c <= b >= a:
    max = b
else:
    max = c
if c >= a <= b:
    min = a
elif c >= b <= a:
    min = b
else:
    min = c

print(max)
print(min)
print((a + b + c) - (max + min))