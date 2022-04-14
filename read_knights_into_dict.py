from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)

print("knight_data['Lancelot'][1]: {}\n".format(knight_data['Lancelot'][1]))

for knight, fields in knight_data.items():
    print(fields[0], knight)
print()


