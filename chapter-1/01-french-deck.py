import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck():
    ranks = list(range(2, 11)) + list('JQKA')
    suits = 'Spades Hearts Clubs Diamonds'.split()

    def __init__(self):
        self._cards = [Card(r, s) for s in self.suits for r in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


if(__name__ == '__main__'):
    psydeck = FrenchDeck()
    print('\nPicking a random card from {} cards'.format(len(psydeck)))
    random_card = random.choice(psydeck)
    print (random_card)

    print('\nSlicing and dicing [:13]')
    print(psydeck[:13])

    print('\nLast card [-1]')
    print(psydeck[-1])

    print('\nIteration')
    for card in psydeck[:6]:
        print(card)

    print('\nReversed Iteration')
    for card in reversed(psydeck[:6]):
        print(card)

    print('\nTruthy Check: {} in deck?'.format(random_card))
    print(random_card in psydeck)

    fake_card = Card('404', 'Card Not Found')
    print('\nTruthy Check: {} in deck?'.format(fake_card))
    print(fake_card in psydeck)

    print('Sorting')

    def chsd_sort(card):
        chsd_suit_values = dict(Clubs=1, Hearts=2, Spades=3, Diamonds=4)
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(chsd_suit_values) + chsd_suit_values[card.suit]
    for card in sorted(psydeck, key=chsd_sort):
        print(card)
