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
# todo: more str methods...
