from decimal import Decimal

x = Decimal(3.14)
print(f"{x = }")

y = Decimal("3.14")
print(f"{y = }")

z = Decimal((0, (3, 1, 4), -2))
print(f"{z = }")
print(z.as_tuple())

inf = Decimal("Infinity")
print(f"{inf = }")

nan = Decimal("NaN")
print(f"{nan = }")
