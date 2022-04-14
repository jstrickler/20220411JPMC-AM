from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        for joker_rank in '1', '2':
            joker = joker_rank, "\U0001F0CF"
            self._cards.append(joker)