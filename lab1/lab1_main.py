import math

e = 10 ** (-4)

a = 3  # range 1
b = 4  # range 2


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


def method_newton(a2, b2):
    try:
        itr = 0
        x0 = (a2 + b2) / 2
        xn = fun(x0)
        xn1 = xn - fun(xn) / fun1(xn)
        while abs(xn1 - xn) > math.pow(10, -5):
            itr += 1
            xn = xn1
            xn1 = xn - fun(xn) / fun1(x0)
        print("Result of Newton method is -> ", xn1)
        print("Number of iteration is -> ", itr)
    except ValueError:
        print("Value not invalidate")


def main():
    method_newton(a, b)


if __name__ == "__main__":
    main()
