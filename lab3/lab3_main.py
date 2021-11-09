# fixed point iteration

# xy - y**2 = 1,
# x**2 * y + y = 5.

# d1 = x - ((1 + y**2) / y)/ (math.ln(y) + 1)
# d2 = y - (5 / (1 + x ** 2))/ ((-10*x)/((1 + x**2)**2))


import math

eps = 0.0001

x0 = -2
y0 = 1

x = (1 + y0 ** 2) / y0
y = 5 / (1 + x0 ** 2)

# d1 = (1 + y ** 2) / y - x
d1 = x - ((1 + y ** 2) / y) / (math.log(y) + 1)
# d2 = 5 / (1 + x ** 2) - y
d2 = y - (5 / (1 + x ** 2)) / ((-10 * x) / ((1 + x ** 2) ** 2))

x0 = x
y0 = y

s = 0
while abs(d1) > eps and abs(d2 > eps):
    s += 1
    x = (1 + y0 ** 2) / y0
    y = 5 / (1 + x0 ** 2)

    d1 = (1 + y ** 2) / y - x
    d2 = 5 / (1 + x0 ** 2) - y

    x0 = x
    y0 = y

print("x = ", x)
print("y = ", y)
