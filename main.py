from table import Table

while True:
    table = Table()
    level = input("Tryb Trudnosci:")
    print("Jezeli potrzebujesz pomocy wpisz 'pomoc'")
    count = 0
    while not table.is_game_won():
        table.print_columns()
        action = input("")
        if "ruch" in action:
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
        elif action == "pobierz":
            count += 1
            table.draw(level)
        elif "dobrane-tabela" in action:
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
        elif "dobrane-zbior" == action:
            count += 1
            table.move_waste_foundation()
        elif "tabela-zbior" in action:
            try:
                count += 1
                command = action.split()
                _, column = command
                column = int(column)
                table.move_table_foundation(column)
            except:
                print("blad")
        elif action == "cofnij":
            count += 1
            table.undo()
        elif action == "pomoc":
            print("Komendy do gry w pasjansa\n")
            print("ruch - przenosi karty z jedenj kolumny do drugie, uzycie 'ruch (numer kolumny z ktorej przenosimy) (numer kolumny do ktorej przenosimy) (ile kart [opcjonalne])'\n")
            print("dobierz - dobiera karte/karty na stos kart 'Dobrane'\n")
            print("dobrane-tabela - przenosi karte ze stosu Dobrane do kolumny, uzycie 'dobrane-tabela (numer kolumny)'\n")
            print("dobrane-zbior - przenosi karte ze stosu Dobrane na stos zbioru kart\n")
            print("tabela-zbior - przenosi karte z kolumny na stos zbioru kart, uzycie 'tabela-zbior (numer kolumny z ktorej przenosimy)'\n")
            print("cofnij - cofa o jedne ruch")
        elif action == "end":
            question = input("czy chcesz harzaczac gre od nowa (tak/nie)?:")
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
