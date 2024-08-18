#! python 3

# deck_sequense.

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)  # from 0 to 51
    return rank_value * len(suit_values) + suit_values[card.suit]
    # clubs,2      0   *       4        +   0   = 0
    # spades,A     12 *         4          + 3  = 51
    # hearts,8     6  *         4       + 2 = 26
    # spades,8      6, *        4       + 3 = 27
    # spades,2      0 *         4       + 3 = 3
    # clubs,A      12 *         4       + 0 = 48
    # This doesn't actually happen, but conceptually:


# for card in sorted(deck,key=spades_high):
#   print(card)

# This doesn't actually happen, but conceptually:
# [
#     (Card("2", "clubs"), 0),
#     (Card("2", "diamonds"), 1),
#     ...(Card("A", "hearts"), 50),
#     (Card("A", "spades"), 51),
# ]
# The sorted() function uses these pairs to sort the cards, then returns just the sorted cards:


deck = FrenchDeck()
