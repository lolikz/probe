form = input()

if form == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())

    p = (a + b + c) / 2

    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif form == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif form == 'круг':
    p = 3.14
    r = float(input())
    S = p * r **2
    print(S)
