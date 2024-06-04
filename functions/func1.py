def rect(d1, d2):
  area = d1 * d2
  perimeter = 2 * d1 + 2 * d2
  price = 1000 * area
  return area, perimeter, price

x, _, _ = rect(2, 5)

print(x)

y = 200
print(isinstance(y, str))