import numpy as np
import matplotlib.pyplot as plt
from sympy import mod_inverse
def printGr(a,b):


    y, x = np.ogrid[-10:10:100j, -10:10:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.show()
def summ(x1, y1, x2, y2, fp):
    t1=y2-y1
    t2=x2-x1


    x3 = ((t1*mod_inverse(t2,fp)%fp)**2-(x1+x2))%fp
    y3 = (-y1+(t1*mod_inverse(t2,fp)%fp)*(x1-x3))%fp
    return x3, y3
def summodinak(x1, y1, a, fp):
    a=a%fp
    t1=3*x1**2+a
    t2=2*y1

    x3 = (t1*mod_inverse(t2,fp)%fp)**2-2*x1
    y3 = -y1+(t1*mod_inverse(t2,fp)%fp)*(x1-x3)
    return x3 % fp, y3 % fp
def pov(x1, y1, fp, count, a):
    zx, zy = x1, y1
    while (count > 1):
        if ((zx == x1)and(zy == y1)):
            zx, zy = summodinak(x1, y1, a, fp)
        else:
            zx, zy = summ(zx, zy, x1, y1, fp)
        count -= 1
    return zx % fp, zy % fp
def tochki(a,b,fp):
    """Нахождение точек"""
    slovar = {a: a ** 2 % fp for a in range(fp)}
    print("z^=")
    print(slovar)
    korni = {y: (y ** 3 + a * y + b) % fp for y in range(fp)}
    print("x0=,y0=")
    for key, value in korni.items():
        print("x", key, "=", key, "     ", "y^2=", value)
    print("Точки")
    for key,value in korni.items():
        for key1,value1 in slovar.items():
            if value==value1:
                print("P",key,"= (",key,key1,")")
def checkSimple(p):
    if p%2==0:
        print("Составное")
    else:
        rs=[i**(p-1)%p for i in range(2,5)]
        if all(r==1 for r in rs):
            print('Простое')
        else:
            print('Составное')
def checkDiskr(a,b,fp):
    y=4*a**3+27*b**2%fp
    print(y)





if __name__ == "__main__":
    while True:
        print('Режим работы:')
        print(' 1 --- Проверить является ли число простым')
        print(' 2 --- Проверить дискриминант')
        print(' 3 --- Найти все точки')
        print(' 4 --- Сложить две точки')
        print(' 5 --- Умножить точку на число')
        print(' 6 --- Вывести график')
        case = input()
        if case == '1':
            print('Введите число: ', end='')
            p = (input())
            checkSimple(int(p))
        elif case == '2':
            a = int((input("Ведите а: ")))
            b = int((input("Ведите b: ")))
            fp= int((input("Ведите поле: ")))
            checkDiskr(a,b,fp)
        elif case == '3':
            a = int((input("Ведите а: ")))
            b = int((input("Ведите b: ")))
            fp = int((input("Ведите поле: ")))
            tochki(a,b,fp)
        elif case == '4':
            x1 = int((input("Ведите x1: ")))
            y1 = int((input("Ведите y1: ")))
            x2= int((input("Ведите x2: ")))
            y2=int((input("Ведите y2: ")))
            fp = int((input("Ведите поле: ")))
            t1 = y2 - y1
            t2 = x2 - x1
            if t1 or t2==0:
                print('besk')
            else:
                print(summ(x1, y1, x2, y2, fp))

        elif case == '5':
            x1 = int((input("Ведите x1: ")))
            y1 = int((input("Ведите y1: ")))
            count = int((input("Ведите множитель: ")))
            a = int((input("Ведите a: ")))
            fp = int((input("Ведите поле: ")))
            print(pov(x1, y1, fp, count, a))
        elif case == '6':
            a = int((input("Ведите a ")))
            b = int((input("Ведите b ")))
            printGr(a,b)

        print('Продолжить? да/нет')
        fail_condition = input()
        if fail_condition == 'нет':
            break


