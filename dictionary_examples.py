d1 = dict()  # empty dict
d2 = {'NC': 'Raleigh', 'CA': 'Sacramento', 'TX': 'Austin'}
d3 = {}  # empty dict
d2['MA'] = 'Boston'
d2['SC'] = 'Columbia'
print("d1: {}".format(d1))
print("d2: {}".format(d2))
print("d3: {}".format(d3))

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

airports['SEA'] = "Seattle-Tacoma"
print("airports: {}".format(airports))
print("len(airports): {}".format(len(airports)))
print('LAX' in airports)

print(airports['OAK'], airports['SMF'])
print(airports.get('LGA'))
print(airports.get('LGA', 'NOT FOUND'))

print(airports.setdefault('LGA', 'LaGuardia'))
print("airports: {}".format(airports))
print(airports.setdefault('RDU', 'Durham'))
print("airports: {}".format(airports))
print()

#  for key, value in DICT.items(): ...
for code, name in airports.items():
    print(code, name)
print('-' * 60)
print("airports.items(): {}".format(airports.items()))





