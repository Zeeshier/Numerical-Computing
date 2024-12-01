# Simple Iterative Method

def iterative_method(g, x0, tol, max_iter):
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return None

# Example: x = sqrt(1 + x)
g = lambda x: (1 + x)**0.5
root = iterative_method(g, 1, 1e-5, 100)
print("(Iterative Method):", root)
