import copy, numpy

a = numpy.array([[2., 2, 1, 1],
                 [1, 2, 1, 1],
                 [0, 1, 1, 2]])
print(a)


def gaussFunc(a):  # В метод передається масив)
    eps = 1e-16

    c = numpy.array(a)
    a = numpy.array(a)  # свторюємо копію масива а

    len1 = len(a[:, 0])  # розмір матриці A, тобто n
    len2 = len(a[0, :])  # n+1
    # vectB = copy.deepcopy(a[:, len1])#вектор B в Ax=B

    for g in range(len1):

        max = abs(a[g][g])
        my = g  # масимум в стовпчику
        t1 = g  # g
        while t1 < len1:  # цикл пошуку максимума в стовпчику
            if abs(a[t1][g]) > max:
                max = abs(a[t1][g])
                my = t1
            t1 += 1

        if abs(max) < eps:
            raise DetermExeption("Check determinant")  # визначник матриці дорівнює 0

        if my != g:
            a[g][:], a[my][:] = a[my][:], a[g][:]  # міняємо дану строчку з строчкою, в якій
            # максимум ( реализация swap())

        amain = float(a[g][g])  # коеф перед x

        z = g
        while z < len2:
            a[g][z] = a[g][z] / amain  # x стає  1
            z += 1
        j = g + 1

        while j < len1:  # віднімаємо строку, помножену на коефіцієнти
            b = a[j][g]  # від настпної, получаємо стовпчик нулів.
            z = g
            while z < len2:
                a[j][z] = a[j][z] - a[g][z] * b
                z += 1
            j += 1

    a = backTrace(a, len1)  # звортній хід метода Гаусса

    print("Похибка:")
    print(vectorN(c, a, len1))
    return a


class DetermExeption(Exception):  # перевірка визначника
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def backTrace(a, len1):  # зворотній хід
    a = numpy.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            a[j][len1] = a[j][len1] - a[j][i] * a[i][len1]
            j -= 1
        i -= 1
    return a[:, len1]


def vectorN(c, a, len1):
    c = numpy.array(c)
    a = numpy.array(a)
    vectB = copy.deepcopy(c[:, len1])
    b = numpy.zeros((len1))
    i = 0

    while i < len1:
        j = 0
        while j < len1:
            b[i] += c[i][j] * a[j]
            j += 1
        i = i + 1

    c = copy.deepcopy(b)

    for i in range(len1):
        c[i] = abs(c[i] - vectB[i])

    return c


b = gaussFunc(a)
print("Відповідь:")
print(b)
