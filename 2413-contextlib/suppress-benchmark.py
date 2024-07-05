from timeit import repeat

try_except = """
try:
    1 / 0
except ZeroDivisionError:
    pass
"""

with_suppress = """
with suppress(ZeroDivisionError):
    1 / 0
"""

t0 = min(repeat(stmt=try_except))
t1 = min(repeat(stmt=with_suppress, setup="from contextlib import suppress"))

print(f"Try/except: {t0:.3f}s")
print(f"  Suppress: {t1:.3f}s")
