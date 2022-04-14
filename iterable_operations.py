
s = "spam"
s += "ham"  #  s = s + "ham"
print("s: {}".format(s))

a = [1, 2, 3]
b = [4, 5, 6]
result = a + b
print("result: {}".format(result))
result += [7, 8]
print("result: {}".format(result))

print('-' * 60)
print("[0] * 10: {}".format([0] * 10))

x = [1, 2, 3] * 3
print("x: {}".format(x))

flags = [True] * 25
print("flags: {}".format(flags))
print()

cities = ['Jersey City', 'Houston', 'Tampa', 'Plano', 'San Francisco']
cities.insert(0, 'Columbus')

for x in 'Durham', 'Houston', 'Milwaukee', 'Plano', 'Rome':
    print(x, x in cities)
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(min(fruits), max(fruits), len(fruits), sorted(fruits), '\n')

print(min(nums), max(nums), len(nums), sorted(nums), sum(nums), '\n')

print("nums: {}\n".format(nums))

rnums = reversed(nums)
print("rnums: {}".format(rnums))

for number in rnums:
    print(number)
print()

x = ['a', 'b', 'c']
ex = enumerate(x)

for i, letter in ex:
    print(i, letter)
print()
enum_x = enumerate(x)
print(list(enum_x))
print(list(enum_x))

print()

for i in range(5):
    print(i, "Wombat!")
print()

#  range(stop)  range(start, stop) range(start, stop, step)
for i in range(1, 6):
    print(i, end=' ')
print('\n\n')












