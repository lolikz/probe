x = float(input())
y = float(input())
z = input()

if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == '/' and y > 0:
    print(x / y)
elif z == '*':
    print(x * y)
elif z == "mod" and y > 0:
    print(x % y)
elif z == "pow" and y > 0:
    print(x ** y)
elif z == "div" and y > 0:
    print(x // y)
else:
    print('Деление на 0!')
