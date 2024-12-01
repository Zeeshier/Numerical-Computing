# Regular Falsi Method

def regula_falsi(func, a, b, tol):
    if func(a) * func(b) >= 0:
        print("Regula Falsi method fails.")
        return None
    while abs(b - a) > tol:
        c = a - (func(a) * (b - a)) / (func(b) - func(a))
        if func(c) == 0:
            return c
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c

# Example
f = lambda x: x**3 - x - 2 
root = regula_falsi(f, 1, 2, 1e-5)
print(" (Regula Falsi):", root)
