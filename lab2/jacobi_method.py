f1 = lambda x, y, z, k: (9 - 2 * y + z - k) / 5
f2 = lambda x, y, z, k: (-10 + x + 2 * k) / 4
f3 = lambda x, y, z, k: (10 + 2 * x + 3 * y - k) / 9
f4 = lambda x, y, z, k: (5 + 3 * x + z) / 6


def jacobi_method():
    x0 = 0
    y0 = 0
    z0 = 0
    k0 = 0
    count = 1

    e = 0.0001

    condition = True

    while condition:
        x1 = f1(x0, y0, z0, k0)
        y1 = f2(x0, y0, z0, k0)
        z1 = f3(x0, y0, z0, k0)
        k1 = f4(x0, y0, z0, k0)
        # print('%d\t%0.4f\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1, y1, z1, k1))
        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)
        e4 = abs(k0 - k1)

        count += 1
        x0 = x1
        y0 = y1
        z0 = z1
        k0 = k1

        condition = e1 > e and e2 > e and e3 > e and e4 > e

    print('\n\nRequired solution by Jacobi Method is:\nX1=%0.3f, X2=%0.3f, X3=%0.3f and X4=%0.3f' % (x1, y1, z1, k1))

