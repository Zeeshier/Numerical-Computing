# Newton-Raphson Method

def newton_raphson(func, dfunc, x0, tol, max_iter):
    for i in range(max_iter):
        x1 = x0 - func(x0) / dfunc(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

# Example
f = lambda x: x**3 - x - 2
df = lambda x: 3 * x**2 - 1
root = newton_raphson(f, df, 1.5, 1e-5, 100)
print("(Newton-Raphson):", root)
