import random
import keyboard


class Card:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name} ({self.value})"


class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards = []
        self.ace_count = 0

    def get_value(self) -> int:
        value = 0
        self.ace_count = 0
        for card in self.cards:
            value += card.value
            if card.name.startswith('A'):
                self.ace_count += 1
        # Корекція для тузів
        while value > 21 and self.ace_count:
            value -= 10
            self.ace_count -= 1
        return value

    def add_card(self, card: Card):
        self.cards.append(card)

    def __repr__(self):
        return f"{self.name}: {self.cards} (Total: {self.get_value()})"


class Game:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10,
              'A': 11}

    def __init__(self, player_name: str):
        self.deck = self.create_deck()
        random.shuffle(self.deck)
        self.player = Player(player_name)
        self.dealer = Player("Dealer")

    def create_deck(self):
        """Створює нову колоду карт"""
        deck = [Card(rank, self.values[rank]) for rank in self.ranks for _ in range(4)]
        return deck

    def deal_card(self, player: Player):
        card = self.deck.pop()
        player.add_card(card)

    def start_game(self):

        for _ in range(2):
            self.deal_card(self.player)
            self.deal_card(self.dealer)
        print(self.player)
        print(self.dealer)

    def player_turn(self):
        while self.player.get_value() < 21:
            print("Press '1' to take a card, or '2' to stand.")
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name == '1':
                self.deal_card(self.player)
                print(self.player)
                if self.player.get_value() > 21:
                    print("You busted! Game over.")
                    return False
            elif event.event_type == keyboard.KEY_DOWN and event.name == '2':
                break
        return True

    def dealer_turn(self):
        print("Dealer's turn:")
        while self.dealer.get_value() < 17:
            self.deal_card(self.dealer)
            print(self.dealer)
        if self.dealer.get_value() > 21:
            print("Dealer busted! You win!")
            return False
        return True

    def determine_winner(self):
        player_value = self.player.get_value()
        dealer_value = self.dealer.get_value()

        print(f"Your total: {player_value}, Dealer's total: {dealer_value}")
        if player_value > 21:
            print("You busted. Dealer wins!")
        elif dealer_value > 21:
            print("Dealer busted. You win!")
        elif player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")


class KeyPress:
    def on_key_event(self):
        game = Game("Player")
        game.start_game()


        if game.player_turn():
            
            if game.dealer_turn():
                game.determine_winner()


# Запуск гри
key_handler = KeyPress()
key_handler.on_key_event()


        

       

        







        
