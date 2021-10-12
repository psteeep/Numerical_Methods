import math


def fun(x):
    """
    default function
    :param x: any argument
    :return: res
    """
    return math.sinh(x) - 12 * math.tanh(x) - 0.311


def g_fun(x):
    pass


def main():
    e = 10 ** (-4)
    a = 0  # range 1
    b = 1  # range 2
    x0 = (a + b) / 2

    F1 = fun(a)
    F2 = fun(b)

    if F1 * F2 > 0:
        itr = 1
        xp = x0
        xn = fun(xp) # g_fun ???
        res = xn - xp
        xp = xn
        while abs(res) < e:
            itr += 1
            xn = g_fun(xp)
            res = xn - xp
            xp = xn
        print("res = ", xp)
        print("itr =", itr)
    else:
        print("no solution")


if __name__ == "__main__":
    main()