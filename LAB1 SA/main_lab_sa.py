import matplotlib.pyplot as plt
import numpy as np
import plots


class RecurrentAlgo:

    def __init__(self, k, a1, a2, b, uk, t0, q):
        self.k = k
        self.a1 = a1
        self.a2 = a2
        self.b = b
        self.uk = uk
        self.input_sign = 0
        self.increase_range = True
        self.t0 = t0
        self.q = q

        self.x0 = np.array([0, 0, 0])
        self.A = np.array([[0, 1, 0],
                           [0, 0, 1],
                           [-1, -a1, -a2]])
        self.B = np.array([0, 0, b])
        self.C = np.array([1, 0, 0])

    def f_decomp(self):
        f = np.identity(3)
        for i in range(self.q):
            f += np.linalg.matrix_power(self.A * self.t0, i + 1) / np.math.factorial(i + 1)
        return f

    def g_decomp(self):
        g = np.identity(3)
        for i in range(self.q - 1):
            g += np.linalg.matrix_power(self.A * self.t0, i + 1) / np.math.factorial(i + 2)
        g = np.dot(g * self.t0 * self.uk, self.B)
        return g

    def get_next_x(self, xk: np.ndarray(shape=(1, 3)), F: np.ndarray(shape=(3, 3)),
                   G: np.ndarray(shape=(1, 3)), uk):  # xk -> xk+1
        return np.dot(F, xk) + G * self.uk

    def getXY(self):
        t = self.input_sign
        if self.input_sign:
            if self.increase_range:
                _range = (self.input_sign + 1) * (input_sign := self.k)
            else:
                self.input_sign = self.k // (self.input_sign + 1)
        X = np.zeros(shape=(self.k, 3))
        Y = np.zeros(shape=(self.k,))
        F = self.f_decomp()
        G = self.g_decomp()
        X[0] = self.x0
        Y[0] = self.x0[0]
        for i in range(1, self.k):
            if self.input_sign and i % self.input_sign == 0:
                self.uk *= -1
            X[i] = self.get_next_x(X[i - 1], F, G, self.uk)
            Y[i] = X[i][0]
        return X, Y


def main():

    print("\t\t***** Enter parameters *****\n\n")
    k = int(input("Enter k = "))
    a1 = int(input("Enter a1 = "))
    a2 = int(input("Enter a2 = "))
    b = int(input("Enter b ="))

    uk = int(input("Enter option:"))

    q = int(input("Enter q = "))
    t0 = float(input("Enter T0 = "))

    rec = RecurrentAlgo(k, a1, a2, b, uk, t0, q)
    X, Y = rec.getXY()
    plots.plot_graph(range(Y.shape[0]), Y)
    plots.print_table(X)


if __name__ == "__main__":
    main()
