from deck import Deck
from table import Table

table = Table()
level = input("tryb trudnosci:")

while not table.is_game_won():
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
        except:
            print("blad")
    elif action == "draw":
        table.draw(level)
    elif "mwt" in action:
        try:
            command = action.split()
            if len(command) == 2:
                _, column = command
                column = int(column)
                move = table.move_waste_column(column)
                if not move:
                    print("Zly ruch")
            else:
                print("Zly format")
                continue
        except:
            print("blad")
    elif "mwf" == action:
        table.move_waste_foundation()
    elif "mtf" in action:
        try:
            command = action.split()
            _, column = command
            column = int(column)
            table.move_table_foundation(column)
        except:
            print("blad")
    elif action == "end":
        break
        
if table.is_game_won():
    table.print_columns()
    print("Wygrales")
