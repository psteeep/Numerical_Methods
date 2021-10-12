# sh(x) - 12th(x) - 0.311 = 0
# eps = 0,0001

# Метод простої ітерації

# Метод Нютона

# Апріорна та апостеріорна  оцінка кількості кроків

# Поч. проміжок та поч. наближення однакове для обох методів

# порівняти результати обох методів між собою

import math

e = 10 ** (-4)

a = 0  # range 1
b = 1 # range 2


def fun(x):
    """
    default function
    :param x: any argument
    :return: res
    """
    return math.sinh(x) - 12 * math.tanh(x) - 0.311


def fun1(x):
    """
    derivative from main function
    :param x: any argument
    :return:
    """
    return math.cosh(x) - 12 * (1 / math.cosh(x) ** 2)


def method_iterations(a1, b1):
    try:
        itr = 0
        x1 = (a1 + b1) / 2  # seed
        a1 = abs((fun(a1 + 0.0001) - fun(a1)) / 0.0001)
        b1 = abs((fun(b1 + 0.0001) - fun(b1)) / 0.0001)

        q = max(a1, b1)
        q = (1 - q) / q
        x0 = x1
        x1 = fun(x0)
        while abs(x1 - x0) <= (q*e):
            itr += 1
            x0 = x1
            x1 = fun(x0)
        return x1, itr
    except ValueError:
        print("Value not invalidate")


def method_newton(a2, b2):
    try:
        itr = 0
        x0 = (a2 + b2) / 2  # seed
        xn = fun(x0)
        xn1 = xn - fun(xn) / fun1(xn)
        while abs(xn1 - xn) > math.pow(10, -5):
            itr += 1
            xn = xn1
            xn1 = xn - fun(xn) / fun1(xn)
        return xn1, itr
    except ValueError:
        print("Value not invalidate")


def main():

    print("Iterations method -> ", method_iterations(a, b))
    print("Newton method -> ",  method_newton(a, b))


if __name__ == "__main__":
    main()