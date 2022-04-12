
# int float (also bool complex)
# numpy/scipy/pandas:  int16, int32, int64, etc

i1 = 1234
i2 = 0
i3 = -12
i4 = 324763209467324234693274672346283946234862346346023462346
print(i4 + 1)

ib = 0b1001  # bin
ix = 0x1001  # hex
io = 0o1001  # oct
print(ib, ix, io, '\n')

a = 19
b = 5
print(a + b, a - b)
print(a * b, a / b, a // b, a / -b, a // -b)
print(a ** b, a % b)

x = 10
x += 5  # x = x + 5
x *= 4
x /= 3
print(x, '\n')


# NOT IMPLEMENTED:  x++  x--  ++x --x

a = "123"
b = 456
print(a + str(b))
print(int(a) + b)
print(float(a) + float(b))

