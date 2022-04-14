set1 = set()
set1.add('blue')
set1.add('green')
set1.add('pink')
set1.add('grey')
set1.add('blue')
set1.add('blue')
set1.add('orange')
set1.add('yellow')
print("set1: {}".format(set1))

colors = ['red', 'blue', 'red', 'red', 'green', 'yellow', 'black']
set2 = set(colors)
print("set2: {}".format(set2))

print("BOTH: set1 & set2: {}".format(set1 & set2)) # intersection
print("JUST ONE: set1 ^ set2: {}".format(set1 ^ set2)) # xor
print("ALL: set1 | set2: {}".format(set1 | set2))  # union
print("JUST set1:", set1 - set2)
print("JUST set2:", set2 - set1)

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
unique_foods = set(food)
print("unique_foods: {}".format(unique_foods))

