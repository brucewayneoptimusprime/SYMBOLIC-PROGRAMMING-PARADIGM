import sympy as sp

# 1. Calculate √2 with 100 decimals.
sqrt_2 = sp.sqrt(2)
sqrt_2_100_decimals = sp.N(sqrt_2, 100)
print(f"√2 with 100 decimals: {sqrt_2_100_decimals}\n")

# 2. Calculate 1/2 + 1/3 in rational arithmetic.
expr = sp.Rational(1, 2) + sp.Rational(1, 3)
print(f"1/2 + 1/3 in rational arithmetic: {expr}\n")

# 3. Calculate the expanded form of (x+y).
x, y = sp.symbols('x y')
expanded_form = sp.expand(x + y)
print(f"Expanded form of (x + y): {expanded_form}\n")

# 4. Simplify the trigonometric expression - sin(x) cos(x).
expr = sp.sin(x) * sp.cos(x)
simplified_expr = sp.simplify(expr)
print(f"Simplified expression - sin(x) * cos(x): {simplified_expr}\n")

# 5. Calculate limit (sin(x)) as x approaches 0.
limit_expr = sp.sin(x)
limit_x_0 = sp.limit(limit_expr, x, 0)
print(f"Limit of sin(x) as x approaches 0: {limit_x_0}\n")

# 6. Calculate the derivative of log(x), 1/x, sin(x), cos(x) for x.
functions = [sp.log(x), 1/x, sp.sin(x), sp.cos(x)]
derivatives = [sp.diff(func, x) for func in functions]
for func, derivative in zip(functions, derivatives):
    print(f"Derivative of {func}: {derivative}\n")

# 7. Solve the system of equations x + y = 2, 2x + y = 0.
eq1 = sp.Eq(x + y, 2)
eq2 = sp.Eq(2*x + y, 0)
solution = sp.solve((eq1, eq2), (x, y))
print(f"Solution to the system of equations: {solution}\n")

# 8. Integrate x, sin(x), cos(x) in terms of x and y.
integrated_x = sp.integrate(x, x)
integrated_sin_x = sp.integrate(sp.sin(x), x)
integrated_cos_x = sp.integrate(sp.cos(x), x)
print(f"Integral of x: {integrated_x}")
print(f"Integral of sin(x): {integrated_sin_x}")
print(f"Integral of cos(x): {integrated_cos_x}\n")

# 9. Solve f'(x) + 9f(x) = 1
f = sp.Function('f')
f_derivative = f(x).diff(x)
equation = sp.Eq(f_derivative + 9*f(x), 1)
solution = sp.dsolve(equation, f(x))
print(f"Solving f'(x) + 9f(x) = 1: {solution}\n")

# 10. Using matrices solve the linear equations 3x+7y=12z, 4x-2y=5z.
x, y, z = sp.symbols('x y z')
eq1 = sp.Eq(3*x + 7*y, 12*z)
eq2 = sp.Eq(4*x - 2*y, 5*z)
coeff_matrix, terms = sp.linear_eq_to_matrix((eq1, eq2), (x, y))
solution = sp.linsolve((coeff_matrix, terms), x, y, z)
print(f"Solving the linear equations using matrices: {solution}")
