from sympy import symbols, Eq, solve

x, y = symbols('x y')

# Define the system of equations
eq1 = Eq(2*x + 3*y, 7)
eq2 = Eq(x - y, 2)

# Solve the system of equations
solutions = solve((eq1, eq2), (x, y))

print(f"Solutions for the system of equations: {solutions}")