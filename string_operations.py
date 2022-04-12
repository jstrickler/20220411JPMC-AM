actor = "Chris Hemsworth"
print(type(actor), actor, len(actor))
print(actor.upper())   # OBJ.method()  function(OBJ)
a2 = actor.upper()
print(actor.upper(), actor.lower(), actor)
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'), actor.startswith('Liam'))
print("Hem" in actor, "Haw" in actor)
print(actor.replace(' ', ''))
print(actor.replace('h', 'o'))
print(actor.isalpha())
print(actor.replace(' ', '').isalpha())
print(actor)
print(actor.find('Chris'), actor.find('Liam'))
print(actor.find('worth'), actor.find('value'))

s = "          My hovercraft is full of eels      "
print("|" + s + "|")
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print('-' * 60)

s = "spam\n"
clean_s = s.rstrip()
print(repr(s), repr(clean_s))   # str(...)
print()

s = "fvcccccccvvfffffffMy hovercraft is full of eelscccfffvfvfvfcccccf"
print("|" + s + "|")
print("|" + s.lstrip("cfv") + "|")
print("|" + s.rstrip("vfc") + "|")
print("|" + s.strip("cvf") + "|")
print('-' * 60)

s = "$1000.00"
clean_s = s.lstrip('$')
print(s, clean_s)

color_data = "blue    pink     orange\tblack\n\ngreen"
colors = color_data.split()
print(colors, '\n')

record = 'Jane:Doe:Ames:IA'
fields = record.split(':')
print(fields)
print('-' * 60)


