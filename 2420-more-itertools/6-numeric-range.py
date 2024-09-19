import datetime as dt

from more_itertools import numeric_range

# for i in numeric_range(10):
#     print(i)

# for j in numeric_range(1.75, 7.1, 1.75):
#     print(j)

start = dt.datetime(2024, 1, 1)
end = dt.datetime(2025, 1, 1)

for date in numeric_range(start, end, dt.timedelta(days=7, seconds=4053)):
    print(date)
