import random
import copy
from deck import Deck

class Table:
    suits = ["♠️", "♥️", "♦️", "♣️"]
    values = ["A"] + [i for i in range(2, 11)] + ["J", "Q", "K"]

    def __init__(self):
        self.deck = Deck()
        self.history = []
        self.foundation = {"♠️": [], "♥️": [], "♦️": [], "♣️": []}
        self.column = [[] for _ in range(7)]
        self.waste = []
        self.used = []

        for i in range(7):
            for j in range(i + 1):
                card = self.deck.draw()
                if card:
                    card.face_up = (j == i)
                    self.column[i].append(card)
        
        for card in self.deck.deck:
            card.face_up = True
    
    def print_columns(self):
        print("\nWaste \t\t    Foundation")
        waste_tab = self.waste[-3:] if self.waste else []
        waste = " ".join(str(card) for card in waste_tab)
        foundation = " ".join(f"{suit}:{self.foundation[suit][-1].value if self.foundation[suit] else '__'}" for suit in self.foundation)
        print(f"{waste}\t\t{foundation:^1}")
        print("\n------------------------------------------")
        for id, col in enumerate(self.column):
            print(f"Kolumna {id + 1}: ", end="")
            print(" ".join(str(card) for card in col))
        print("------------------------------------------")

    def move_card_columns(self, from_col, to_col, num_cards = 1):
        self.save()

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
            
        target_card = self.column[to_col][-1]

        if not self.is_valid_move(cards[0], target_card):
            self.column[from_col].extend(cards)
            return False
            
        self.column[to_col].extend(cards)

        if self.column[from_col]:
            self.column[from_col][-1].face_up = True

        return True
    
    def is_valid_move(self, card_column, target_column):
        
        card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

        if (card_column.suit in ["♥️", "♦️"] and target_column.suit in ["♥️", "♦️"]) or (card_column.suit in ["♣️", "♠️"] and target_column.suit in ["♣️", "♠️"]):
            return False

        if card_values[str(target_column.value)] - 1 != card_values[str(card_column.value)]:
            return False
        
        return True

    def draw(self, level):
        self.save()

        if not self.deck.deck:
            if not self.used:
                print("All cards used")
                return
            random.shuffle(self.used)
            self.deck.deck = self.used[:]
            self.used = []
        if level == "easy":
            if self.waste:
                self.used.extend(self.waste)
                self.waste = []
            self.waste.append(self.deck.draw())
        elif level == "hard":
            if self.waste:
                self.used.extend(self.waste)
                self.waste = []
            for _ in range(3):
                card = self.deck.draw()
                if card:
                    self.waste.append(card)

    def move_waste_column(self, column):
        self.save()

        column = column - 1
        waste = self.waste[-1]

        if not waste:
            return False
        
        if not self.column[column]:
            if waste.value == "K":
                self.column[column].append(waste)
                self.waste.pop()
                return True
            else:
                return False
            
        card = self.column[column][-1]
        
        if not self.is_valid_move(waste, card):
            return False
        
        self.column[column].append(waste)
        self.waste.pop()
        return True
    
    def move_waste_foundation(self):
        self.save()

        card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

        if not self.waste:
            print("nie masz kart na stosie dobranych")
            return
        
        card = self.waste[-1]
        foundation_pile = self.foundation[card.suit]

        if not foundation_pile:
            if card.value != "A":
                print("Musisz najpierw miec wstawionego Asa")
                return
        else:
            foundation_top = foundation_pile[-1]
            if card_values[str(card.value)] != card_values[str(foundation_top.value)] + 1:
                print("Musisz postawic karte o jeden wyzsza")
                return
        
        self.waste.pop()
        self.foundation[card.suit].append(card)

    def move_table_foundation(self, column):
        self.save()
        card_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

        column = column - 1
        card = self.column[column][-1]

        if not card:
            print("nie masz tutaj karty")
            return
        
        foundation_pile = self.foundation[card.suit]
        
        if not foundation_pile:
            if card.value != "A":
                print("Musisz najpierw miec wstawionego Asa")
                return
        else:
            foundation_top = foundation_pile[-1]
            if card_values[str(card.value)] != card_values[str(foundation_top.value)] + 1:
                print("Musisz postawic karte o jeden wyzsza")
                return
            
        self.column[column].pop()
        self.foundation[card.suit].append(card)

        if self.column[column]:
            self.column[column][-1].face_up = True

    def save(self):
        state = {
            "deck": copy.deepcopy(self.deck),
            "foundation": copy.deepcopy(self.foundation),
            "column": copy.deepcopy(self.column),
            "waste": copy.deepcopy(self.waste),
            "used": copy.deepcopy(self.used)
        }
        self.history.append(state)
        if len(self.history) > 3:
            self.history.pop(0)

    def undo(self):
        if not self.history:
            print("Brak ruchow do cofniecia")
            return
        
        last_state = self.history.pop()
        self.deck = last_state["deck"]
        self.foundation = last_state["foundation"]
        self.column = last_state["column"]
        self.waste = last_state["waste"]
        self.used = last_state["used"]

    def is_game_won(self):
        total = sum(len(pile) for pile in self.foundation.values())
        return total == 52
    