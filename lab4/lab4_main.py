# інтерполяційний поліном у формі Лагранджа та Нютона
# вузли які є нулями поліному Чебешева
# 15 вузлів


import matplotlib.pyplot as plt
import math
import numpy as np


def lagrange(x_, y, a):
    ans = 0.0
    for i in range(len(y)):
        t_ = y[i]
        for j in range(len(y)):
            if i != j:
                t_ *= (a - x_[j]) / (x_[i] - x_[j])
        ans += t_
    return ans


def table(x_, y):
    quotient = [[0] * len(x_) for _ in range(len(x_))]
    for n_ in range(len(x_)):
        quotient[n_][0] = y[n_]
    for i in range(1, len(x_)):
        for j in range(i, len(x_)):
            quotient[j][i] = (quotient[j][i - 1] - quotient[j - 1][i - 1]) / (x_[j] - x_[j - i])
    return quotient


def get_corner(result):
    link = []
    for i in range(len(result)):
        link.append(result[i][i])
    return link


def newton(data_set, x_p, x_7):
    result = data_set[0]
    for i in range(1, len(data_set)):
        p = data_set[i]
        for j in range(i):
            p *= (x_p - x_7[j])
        result += p
    return result


if __name__ == '__main__':
    x = 2.5

    x_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    y_1 = [0, 0.8415, 0.9093, 0.1411, -0.7568, -0.9589, -0.2794, -0.9163, -0.6931, -0.5108, -0.3567, -0.2231, 0.2322,
                0.5242, -0.5365]
           # x_1 = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014]
           # y_1 = [121.093, 121.092, 121.091, 121.090, 121.090, 121.089, 121.084, 121.079,
           #121.081, 121.080, 121.079, 121.078, 121.074, 121.070, 121.069]
    middle = table(x_1, y_1)
    n = get_corner(middle)
    newton = newton(n, x, x_1)
    lagrange = lagrange(x_1, y_1, 2.5)

    print("Lagrange Interpolating Polynomial: {}".format(lagrange))
    print("Newton Interpolating Polynomial: {}".format(newton))
