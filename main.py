def main():
    is_game_on = True
    while is_game_on:
        game_table = [' '] * 10
        player_no = 1
        game_table = start(player_no, game_table)
        print('Game is Over!')
        print('---This is the final result----')
        display(game_table)
        is_game_on = is_replay()


def is_replay():
    replay = input("Please press R for replay!").upper()
    if replay == "R":
        return True
    else:
        return False


def start(player_no, game_table):
    display_welcome_message()
    display_possible_items()
    display_possible_positions()
    while not is_finished(game_table):
        display(game_table)
        game_table = play(player_no, game_table)
        player_no = change_player(player_no)
    return game_table


def display_welcome_message():
    print('***************************')
    print('Welcome to TIC TAC TOE Game')
    print('***************************')


def display_possible_items():
    print('Please make your X or O move')
    print('***************************')


def display_possible_positions():
    possible_moves = range(1, 10)
    print('Please select your next move position numbers')
    display(possible_moves)
    print('***************************')


def change_player(player_no):
    if player_no == 2:
        return 1
    else:
        return 2


def play(player_no, game_table):
    next_move = get_move(player_no, game_table)
    return move(game_table, next_move)


def get_move(player_no, game_table):
    position = get_position(player_no, game_table)
    item = get_item(player_no)
    return position, item


def get_item(player_no):
    while True:
        item = input('Player{} please enter your next item'.format(player_no))
        if is_proper_item(item):
            break
        else:
            display_possible_items()
    return item


def get_position(player_no, game_table):
    while True:
        try:
            position = int(input('Player{} please enter your next item position'.format(player_no)))
            if is_proper_position(position, game_table):
                break
            else:
                display_possible_positions()
        except ValueError:
            display_possible_positions()
    return position


def is_proper_position(position, game_table):
    for i in range(1, 10):
        if i == position and game_table[i - 1] == ' ':
            return True
    return False


def is_proper_item(item):
    if item == 'X' or item == 'O':
        return True
    else:
        return False


def move(game_table, next_move):
    position = next_move[0]
    item = next_move[1]
    game_table[position - 1] = item
    return game_table


def display(table):
    row = ''
    for index, value in enumerate(table):
        row += str(value) + ' | '
        if (index + 1) % 3 == 0:
            print(row)
            row = ''


def is_finished(game_table):
    return is_board_full(game_table) or is_column_match(game_table) or is_row_match(game_table) or is_cross_match(
        game_table)


def is_board_full(game_table):
    for place in game_table:
        if place == ' ':
            return False
    return True


def is_column_match(game_table):
    for i in range(0, 3):
        if game_table[i] == game_table[i + 3] and game_table[i + 3] == game_table[i + 6] and game_table[i + 6] != ' ':
            return True
    return False


def is_row_match(game_table):
    row_number = [0, 3, 6]
    for i in row_number:
        if game_table[i] == game_table[i + 1] and game_table[i + 1] == game_table[i + 2] and game_table[i + 2] != ' ':
            return True
    return False


def is_cross_match(game_table):
    if game_table[0] == game_table[4] and game_table[4] == game_table[8] and game_table[8] != ' ':
        return True
    if game_table[2] == game_table[4] and game_table[4] == game_table[6] and game_table[6] != ' ':
        return True
    else:
        return False


main()
