import sys

print("sys.argv: {}".format(sys.argv))
print("sys.argv[0]: {}".format(sys.argv[0]))
print("sys.argv[1]: {}".format(sys.argv[1]))
raw_value = sys.argv[1]
value = int(raw_value)
print(repr(raw_value), repr(value))

