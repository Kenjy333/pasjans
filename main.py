import random

'''
clearowanie consoli
print("\033c")
'''
colors = ["♠️", "♦️", "♣️", "♥️"]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
columns = {}

# 28 tyle kart idzie do kolumn

def create_game_cards():
    cards = [f"{w}{k}" for w in values for k in colors]
    random.shuffle(cards)
    for i in range(7):
        hidden = [cards.pop() for _ in range(i)]
        visible = [cards.pop()]
        columns[i + 1] = {
            "hidden": hidden,
            "visible": visible
        }
    return columns

def show_cards(columns):
    print("")
    for column, cards in columns.items():
        hidden_len = len(cards["hidden"])
        hidden = "XX " * hidden_len
        visible = " ".join(cards["visible"])
        print(f"Kolumna {column}: {hidden}{visible}")
    print("")

def start_game():
    game_type = input("Jaki poziom trudności? Łatwy/Trudny:")
    columns = create_game_cards()
    show_cards(columns)
    while True:
        action = input("Co chcesz zrobic? [przestawic/dobrac/koniec]:")
        if action == "koniec":
            break
        elif:

start_game()