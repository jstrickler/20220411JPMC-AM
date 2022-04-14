from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Fred")
# CardDeck d1 = new CardDeck();
d2 = CardDeck("Srini")

print(d1)
# x = what_am_i()
print(d1.get_dealer())

print(d1.dealer)

d1.dealer = 'Dora'
print(d1.dealer)

d1.shuffle()
print(d1.cards)
for _ in range(10):
    card = d1.draw()
    print(card)

print(len(d1))
print(d1)
print(d2)
print('-' * 60)

j1 = JokerDeck("Nellie")
j1.shuffle()
print(j1.cards)
print(j1)


