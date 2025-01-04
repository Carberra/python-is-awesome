from decimal import Decimal as D

x = D("1.30") + D("10.50")
print(f"{x = }")

y = D("0.1") + D("0.1") + D("0.1") - D("0.3")
print(f"{y = }")

print(f"{x > y = }")

z = D("64")
print(z.sqrt())
print(z.exp())
print(z.log10())

w = D("1234.567")
print(w.as_integer_ratio())
print(w.quantize(D("2.2")))
