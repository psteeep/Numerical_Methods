# задача Коші методо Рунге-Кутта 2го порядку точності
# знайти перші 10 значень

# "dy/dx = (x - y)/2"
def dydx(x, y):
    return (x + y - 2)


def rungeKutta(x0, y0, x, h):
    n = round((x - x0) / h)

    y = y0

    for i in range(1, n + 1):
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)


        y = y + (1.0 / 6.0) * (k1 + 2 * k2)
        print(y)

        x0 = x0 + h

    return y


if __name__ == "__main__":
    x0 = 0
    y = 1
    x = 2
    h = 0.2

    print("y(x) =", rungeKutta(x0, y, x, h))
