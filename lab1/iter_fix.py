import math


def fun(x):
    """
    default function
    :param x: any argument
    :return: res
    """
    return math.sinh(x) - 12 * math.tanh(x) - 0.311


def g_fun(x):
    # return (math.sinh(x) - 12 * math.tanh(x) - 0.311)*math.e**(-x) + x
    # return math.e ** (-x)
    return x - fun(x) / fun1(x)


def fun1(x):
    """
    derivative from main function
    :param x: any argument
    :return:
    """
    return math.cosh(x) - 12 * (1 / math.cosh(x) ** 2)


def main():
    e = 10 ** (-4)
    a = 3  # range 1
    b = 4  # range 2
    x0 = (a + b) / 2

    F1 = fun(a)
    F2 = fun(b)

    if F1 * F2 < 0:
        itr = 1
        xp = x0
        xn = g_fun(xp)
        res = xn - xp
        xp = xn
        while abs(res) > e:
            itr += 1
            xn = g_fun(xp)
            res = xn - xp
            xp = xn
            print(xp)
        print("Result of Fixed point method is  -> ", xp)
        print("Number of iteration (posteriori ) is ->", itr)
        print("prior =", int(math.log10(abs(fun(x0) - x0) / e) / (math.log10(1) + 1)+1))
    else:
        print("No solution!")


if __name__ == "__main__":
    main()
