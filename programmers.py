n = int(input())

if n % 100 == 11 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14:
    print(n, 'программистов')
elif n % 10 == 1:
    print(n, 'программист')
elif n % 10 == 2:
    print(n, 'программиста')
elif n % 10 == 3:
    print(n, 'программиста')
elif n % 10 == 4:
    print(n, 'программиста')
else:
    print(n, 'программистов')
