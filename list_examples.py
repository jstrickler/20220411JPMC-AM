list1 = list()   # new, empty, list
list2 = ['spam', 'ham', 'toast']
print(list2[1])
list3 = []   # empty list
#  list(iterable)
# iterable => any object that you can iterate over (with a for loop)

cities = ['Jersey City', 'Houston', 'Tampa', 'Plano', 'San Francisco']
cities.insert(0, 'Columbus')
cities.insert(3, 'NYC')
print("cities: {}".format(cities))
cities.append('Glasgow')
cities.append('Dallas')
print("cities: {}".format(cities))
more_cities = ['Waterloo', 'Montreal', 'Oaxaca']
cities.extend(more_cities)
print("cities: {}".format(cities))

#  LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)

del cities[1]
print("cities: {}".format(cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(5)
print("city: {}".format(city))
print("cities: {}".format(cities))

cities.remove('NYC')
cities.remove('Dallas')
print("cities: {}".format(cities))

#  del LIST[pos]    LIST.pop(pos=-1)   LIST.remove(value)

print(cities[0], cities[3], cities[-1])
print(cities[len(cities)-1])
# print(cities[99])

print("cities[0:4]: {}".format(cities[0:4]))   #  cities[0] through cities[3]
#   [start:stop]   [:stop]  [start:]
print("cities[3:7]: {}".format(cities[3:6]))
print("cities[5:99]: {}".format(cities[5:99]))
print("cities[4:]: {}".format(cities[4:]))

s = "Python"
print("s: {}".format(s))
print("s[:3]: {}".format(s[:3]))
print("s[2:5]: {}".format(s[2:5]))

print("cities: {}".format(cities))

# for VAR in ITERABLE:
#    code...
for city in cities:
    # city = next element of cities
    print(city)
print()

s = "abcd"
for letter in s:
    print(letter)
print()



