import decimal
from decimal import Context, Decimal

print(decimal.getcontext())

decimal.getcontext().prec = 250  # Default is 28

x = Decimal(1) / Decimal(7)
print(x)

y = Decimal("rickroll", context=Context(traps=[]))
print(y)
