# Bisection method

def bisection_method(func, a, b, tol):
    if func(a) * func(b) >= 0:
        print("Bisection method fails.")
        return None
    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2

# Example
f = lambda x: x**3 - x - 2
root = bisection_method(f, 1, 2, 1e-5)
print(" (Bisection):", root)
