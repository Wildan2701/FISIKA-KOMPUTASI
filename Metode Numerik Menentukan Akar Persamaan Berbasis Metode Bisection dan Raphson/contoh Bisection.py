from bisection import*

def f(x):
    y = x**2-4
    return y

a=float(input('Tebakan Awal a = '))
b=float(input('Tebakan Awal b = '))
tol = float(input('Toleransi = '))

x = bisection(f,a,b,tol)
print ("Akar Persamaan: x = {}".format(x))
