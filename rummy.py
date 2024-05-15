import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def draw_from(self, deck, discard_pile):
        if not deck.cards:
            if discard_pile:
                discard_index = int(input("Discard pile is not empty. Enter index of card to pick (or -1 to pass): "))
                if 0 <= discard_index < len(discard_pile):
                    self.hand.append(discard_pile.pop(discard_index))
        else:
            self.hand.append(deck.draw_card())

    def discard(self, discard_pile):
        discard_index = int(input(f"{self.name}'s turn: Choose a card to discard (by index): "))
        discarded_card = self.hand.pop(discard_index)
        discard_pile.append(discarded_card)

    def is_set(self, meld):
        return all(card.rank == meld[0].rank for card in meld)

    def is_run(self, meld):
        sorted_meld = sorted(meld, key=lambda x: x.rank)
        return all(sorted_meld[i].rank == sorted_meld[i + 1].rank - 1 for i in range(len(sorted_meld) - 1))

    def is_valid_meld(self, meld):
        if len(meld) < 3:
            return False
        return self.is_set(meld) or (self.is_run(meld) and all(card.suit == meld[0].suit for card in meld))

    def is_valid_lay_off(self, card, meld):
        if len(meld) == 0:
            return False
        if self.is_set(meld):
            return card.rank == meld[0].rank
        elif self.is_run(meld):
            sorted_meld = sorted(meld, key=lambda x: x.rank)
            return card.suit == sorted_meld[0].suit and card.rank in [c.rank for c in sorted_meld]
        return False

    def meld(self, meld):
        if self.is_valid_meld(meld):
            meld_bonus = 15 if self.is_set(meld) else 20
            self.score += meld_bonus
            for card in meld:
                self.hand.remove(card)
        else:
            print("Invalid meld.")

    def lay_off(self, card, meld):
        if self.is_valid_lay_off(card, meld):
            meld.append(card)
            self.hand.remove(card)
        else:
            print("Invalid lay off.")

    def calculate_score(self):
        point_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        for card in self.hand:
            self.score += point_values.get(card.rank, 0)

def game_over(players):
    for player in players:
        if not player.hand:
            return True
    return False

def main():
    deck = Deck()
    discard_pile = []
    players = [Player("Player 1"), Player("Player 2")]
    for _ in range(7):
        for player in players:
            player.draw_from(deck, discard_pile)
    while not game_over(players):
        for player in players:
            print(f"{player.name}'s hand: {player.hand}")
            player.draw_from(deck, discard_pile)
            player.discard(discard_pile)
            print(f"{player.name}'s discard: {discard_pile[-1]}")
    print("Game over!")

if __name__ == "__main__":
    main()
