import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Game:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.create_deck()

    def create_deck(self):
        self.deck = [Card(value, suit) for suit in self.suits for value in self.values]
        random.shuffle(self.deck)

    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.append(self.deck.pop())
            self.dealer_hand.append(self.deck.pop())

    def calculate_hand_value(self, hand):
        value = 0
        aces = 0
        
        for card in hand:
            if card.value in ['J', 'Q', 'K']:
                value += 10
            elif card.value == 'A':
                aces += 1
            else:
                value += int(card.value)

        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
                
        return value

    def play(self):
        print("Welcome to Blackjack!")
        self.deal_initial_cards()

        while True:
            print("\nYour hand:")
            for card in self.player_hand:
                print(card)
            print(f"Total value: {self.calculate_hand_value(self.player_hand)}")

            if self.calculate_hand_value(self.player_hand) > 21:
                print("Bust! You lose!")
                return

            action = input("\nDo you want to 'hit' or 'stand'? ").lower()
            if action == 'hit':
                self.player_hand.append(self.deck.pop())
            elif action == 'stand':
                break

        print("\nDealer's hand:")
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.pop())

        for card in self.dealer_hand:
            print(card)
        print(f"Dealer's total: {self.calculate_hand_value(self.dealer_hand)}")

        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if dealer_value > 21:
            print("Dealer busts! You win!")
        elif player_value > dealer_value:
            print("You win!")
        elif dealer_value > player_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    game = Game()
    game.play()