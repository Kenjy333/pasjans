from deck import Deck
from table import Table

table = Table()

while True:
    table.print_columns()
    action = input("")
    if "mv" in action:
        try:
            command = action.split()
            if len(command) == 3:
                _, card, target = command
                num_cards = 1
            elif len(command) == 4:
                _, card, target, num_cards = command
            else:
                print("Zły format")
                continue
            move = table.move_card_columns(int(card), int(target), int(num_cards))
            if not move:
                print("Zły ruch")
        except Exception as e:
            print("Błąd:", e)
