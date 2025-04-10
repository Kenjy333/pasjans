from deck import Deck

class Table:
    suits = ["♠️", "♥️", "♦️", "♣️"]
    values = ["A"] + [i for i in range(2, 11)] + ["J", "Q", "K"]

    def __init__(self):
        self.deck = Deck()
        self.foundation = {"♠️": [], "♥️": [], "♦️": [], "♣️": []}
        self.column = [[] for _ in range(7)]
        self.waste = []

        for i in range(7):
            for j in range(i + 1):
                card = self.deck.draw()
                if card:
                    card.face_up = (j == i)
                    self.column[i].append(card)
    
    def print_columns(self):
        print("\nWaste \t\t    Foundation")
        waste = str(self.waste[-1]) if self.waste else None
        foundation = " ".join(f"{suit}:{self.foundation[suit][-1] if self.foundation[suit] else '__'}" for suit in self.foundation)
        print(f"{waste}\t\t{foundation}")
        print("\n------------------------------------------")
        for id, col in enumerate(self.column):
            print(f"Kolumna {id + 1}: ", end="")
            print(" ".join(str(card) for card in col))
        print("------------------------------------------")

    def move_card_columns(self, from_col, to_col, num_cards = 1):
        from_col = from_col - 1
        to_col = to_col - 1

        if len(self.column[from_col]) < num_cards:
            return False

        cards = self.column[from_col][-num_cards:]

        if any(not card.face_up for card in cards):
            return False
        
        self.column[from_col] = self.column[from_col][:-num_cards]
        
        if not self.column[to_col]:
            if cards[0].value == "K":
                self.column[to_col].extend(cards)
                if self.column[from_col]:
                    self.column[from_col][-1].face_up = True
                return True
            else:
                self.column[from_col].extend(cards)
                return False
            
        target = self.column[to_col][-1]
        print("tutaj")
        if not self.is_valid_move(cards[0], target):
            self.column[from_col].extend(cards)
            return False
        
        print(self.column[to_col])
        self.column[to_col].extend(cards)
        print(self.column[to_col])

        if self.column[from_col]:
            self.column[from_col][-1].face_up = True

        return True
    
    def is_valid_move(self, card, target_card):
        card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

        if (card.suit in ["♥️", "♦️"] and target_card.suit in ["♥️", "♦️"]) or (card.suit in ["♣️", "♠️"] and target_card.suit in ["♣️", "♠️"]):
            return False
        
        if card_values[target_card.value] != card_values[card.value] - 1:
            return False
        return True
