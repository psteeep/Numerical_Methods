# var 27

class Quadrature:
    __sum = 0.0
    __nseg = 6
    __ncalls = 0

    def __restart(func, x0, x1, nseg0, reset_calls=True):
        if reset_calls:
            Quadrature.__ncalls = 0
        Quadrature.__nseg = nseg0
        Quadrature.__sum = 0.5 * (func(x0) + func(x1))
        dx = 1.0 * (x1 - x0) / nseg0
        for i in range(1, nseg0):
            Quadrature.__sum += func(x0 + i * dx)

        Quadrature.__ncalls += 1 + nseg0
        return Quadrature.__sum * dx

    def __double_nseg(func, x0, x1):
        nseg = Quadrature.__nseg
        dx = (x1 - x0) / nseg
        x = x0 + 0.5 * dx
        i = 0
        AddedSum = 0.0
        for i in range(nseg):
            AddedSum += func(x + i * dx)

        Quadrature.__sum += AddedSum
        Quadrature.__nseg *= 2
        Quadrature.__ncalls += nseg
        return Quadrature.__sum * 0.5 * dx

    def trapezoid(func, x0, x1, rtol=0.1, nseg0=6):
        ans = Quadrature.__restart(func, x0, x1, nseg0)
        old_ans = 0.0
        err_est = max(1, abs(ans))
        while (err_est > abs(rtol * ans)):
            old_ans = ans
            ans = Quadrature.__double_nseg(func, x0, x1)
            err_est = abs(old_ans - ans)

        # print("Total function calls: " + str(Quadrature.__ncalls))
        return ans


def f(x):
    return 1 / (9 - x)


start = Quadrature

print("result: ", start.trapezoid(f, 4, 7))
