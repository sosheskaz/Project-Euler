#!/usr/bin/env python3
import itertools


def main():
    matchups = list(parse_file())

    wins = len([matchup for matchup in matchups if matchup[0] > matchup[1]])
    print(wins)


def parse_file():
    with open('p054_poker.txt') as f:
        for line in f:
            cards_txt = line.split(' ')
            hand1 = Hand([Card(card_txt) for card_txt in cards_txt[:5]])
            hand2 = Hand([Card(card_txt) for card_txt in cards_txt[5:]])
            yield (hand1, hand2)


class Hand:
    is_rf = None
    is_sf = None
    is_st = None
    is_fl = None
    is_fh = False
    is_4k = False
    is_2p = False
    is_3k = False
    is_pr = False

    def __init__(self, cards):
        cards = [card if isinstance(card, Card) else Card(card) for card in cards]
        self.cards = sorted(cards)

        self.highcard = self.cards[4]
        self.pairs = []
        self.threes = []
        self.fours = []
        grouped = itertools.groupby(self.cards, lambda x: x.value)
        for _, cards in grouped:
            cards = list(cards)
            if len(cards) == 2:
                self.pairs.append(cards)
            elif len(cards) == 3:
                self.threes.append(cards)
            elif len(cards) == 4:
                self.fours.append(cards)
        if self.fours:
            self.is_4k = True
        if self.threes:
            self.is_3k = True
        if self.pairs:
            self.is_pr = True
        if len(self.pairs) == 2:
            self.is_2p = True
        if self.pairs and self.threes:
            self.is_fh = True

    @property
    def values(self):
        return [card.value for card in self.cards]

    @property
    def is_royal_flush(self):
        if self.is_rf == None:
            self.is_rf = {card.value for card in self.cards} == {10, 11, 12, 13, 14} and self.is_flush
        return self.is_rf

    @property
    def is_straight_flush(self):
        if self.is_sf == None:
            self.is_sf = self.is_straight and self.is_flush
        return self.is_sf

    @property
    def is_full_house(self):
        if self.is_fh == None:
            self.is_fh = self.is_3k and self.is_pr
        return self.is_fh

    @property
    def is_straight(self):
        if self.is_st == None:
            values = self.values
            zipped = zip(values[1:], values)
            deltas = [item[1] - item[0] + 1 for item in zipped]
            # All of the deltas between cards are 1
            self.is_st = not any(deltas)
        return self.is_st

    @property
    def is_flush(self):
        if self.is_fl == None:
            self.is_fl = len(list(itertools.groupby(self.cards, lambda x: x.suit))) == 1
        return self.is_fl

    def highcard_gt(self, other):
        for us, them in zip(reversed(self.cards), reversed(other.cards)):
            if us > them:
                return True
            if them > us:
                return False
        return False

    def __gt__(self, other):
        attrs = ['is_royal_flush', 'is_straight_flush', 'is_4k', 'is_full_house', 'is_flush', 'is_straight', 'is_3k', 'is_2p', 'is_pr']
        for attr in attrs:
            if getattr(self, attr) != getattr(other, attr):
                return getattr(self, attr) > getattr(other, attr)
            if not getattr(self, attr) and not getattr(other, attr):
                continue
            # Things that require custom high card logic are done here.

            # These hands require all 5 cards, so highcard is the victor.
            if 'is_straight' in attr or '_flush' in attr:
                return self.highcard_gt(other)

            # 4 of a kind high card is more important
            if 'is_4k' == attr:
                if self.fours[0][0].value != other.fours[0][0].value:
                    return self.fours[0][0].value > other.fours[0][0].value
                return self.highcard_gt(other)
            # 3 of a kind high card, then pair high card.
            if 'is_full_house' == attr:
                if self.threes[0][0].value != other.threes[0][0].value:
                    return self.threes[0][0].value > other.threes[0][0].value
                return self.pairs[-1][0].value > other.pairs[-1].value
            if 'is_3k' == attr:
                if self.threes[0][0].value != other.threes[0][0].value:
                    return self.threes[0][0].value > other.threes[0][0].value
                return self.highcard_gt(other)
            if 'is_2p' == attr:
                for i in [1, 0]:
                    if self.pairs[i][0].value != other.pairs[i][0]:
                        return self.pairs[i][0].value > other.pairs[i][0].value
                return self.highcard > other.highcard
            if 'is_pr' == attr:
                if self.pairs[0][0].value != other.pairs[0][0].value:
                    return self.pairs[0][0].value > other.pairs[0][0].value
                return self.highcard_gt(other)

        return self.highcard_gt(other)


    def __lt__(self, other):
        return not other > self

    def __str__(self):
        return ' '.join(str(card) for card in self.cards)


class Card:
    str2int = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    int2str = {value: key for key, value in str2int.items()}

    def __init__(self, rep):
        if str.isalpha(rep[0]):
            self.value = self.str2int[rep[0]]
        else:
            self.value = int(rep[0])
        self.suit = rep[1]

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return other.value > self.value

    def __str__(self):
        if self.value >= 10:
            value = self.int2str[self.value]
        else:
            value = self.value
        return '{}{}'.format(value, self.suit)

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    main()
