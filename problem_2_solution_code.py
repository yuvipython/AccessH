__author__ = "Yuvi"

x, y = 1, 1
Fibonacci_values = []

while y < 5000000:
    x, y = y, x + y
    Fibonacci_values.append(x)

sum_of_even_valued_terms = sum(filter(lambda n: n % 2 == 0, Fibonacci_values))

print(sum_of_even_valued_terms)
