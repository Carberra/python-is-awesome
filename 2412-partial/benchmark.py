from timeit import repeat

setup_lambda = """
from operator import mul

double = lambda y: mul(2, y)
"""

t0 = min(repeat("double(5)", setup=setup_lambda))

setup_partial = """
from functools import partial
from operator import mul

double = partial(mul, 2)
"""

t1 = min(repeat("double(5)", setup=setup_partial))

print(" Lambda:", t0)
print("Partial:", t1)
print(f"\nPartial is {t0 / t1:.2f} times faster")
