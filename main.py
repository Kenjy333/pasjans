from table import Table

while True:
    table = Table()
    level = input("tryb trudnosci:")
    print("Jezeli potrzebujesz pomocy wpisz 'help'")
    count = 0
    while not table.is_game_won():
        table.print_columns()
        action = input("")
        if "mv" in action:
            try:
                count += 1
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
            count += 1
            table.draw(level)
        elif "mwt" in action:
            try:
                count += 1
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
            count += 1
            table.move_waste_foundation()
        elif "mtf" in action:
            try:
                count += 1
                command = action.split()
                _, column = command
                column = int(column)
                table.move_table_foundation(column)
            except:
                print("blad")
        elif action == "back":
            count += 1
            table.undo()
        elif action == "help":
            print("Komendy do gry w pasjansa\n")
            print("mv - przenosi karty z jedenj kolumny do drugie, uzycie 'mv (numer kolumny z ktorej przenosimy) (numer kolumny do ktorej przenosimy) (ile kart [opcjonalne])'\n")
            print("draw - dobiera karte/karty na stos kart 'waste'\n")
            print("mwt - przenosi karte ze stosu waste do kolumny, uzycie 'mwt (numer kolumny)'\n")
            print("mwf - przenosi karte ze stosu waste na stos foundation\n")
            print("mtf - przenosi karte z kolumny na stos foundation, uzycie 'mtf (numer kolumny z ktorej przenosimy)'\n")
            print("back - cofa o jedne ruch")
        elif action == "end":
            question = input("czy chcesz zaczac gre od nowa (tak/nie)?:")
            if question.lower() == "nie":
                exit()
            elif question.lower() == "tak":
                break

    if table.is_game_won():
        table.print_columns()
        print("Wygrales")
        with open("ranking.txt", "r+") as f:
            f.write(f"Liczba ruchow: {count}\n")
            print("----- RANKING -----")
            for text in f:
                print("text\n")
