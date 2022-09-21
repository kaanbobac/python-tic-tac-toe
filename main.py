DEFAULT_PLACEHOLDER = ' '
POSSIBLE_MARKERS = ['X', 'O']
REPLAY = "R"
PLAYER_NO = [1, 2]


def main():
    is_game_on = True
    while is_game_on:
        final_result = play_the_game()
        print('Game is Over!')
        print('---This is the final result----')
        display(final_result)
        is_game_on = is_replay()


def is_replay():
    choice = input("Please press {} for replay!".format(REPLAY)).upper()
    return True if choice == REPLAY else False


def play_the_game():
    game_table = [DEFAULT_PLACEHOLDER] * 9
    player_no = PLAYER_NO[0]
    display_welcome_message()
    display_possible_markers()
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


def display_possible_markers():
    print('Please make your {} or {} move'.format(POSSIBLE_MARKERS[0], POSSIBLE_MARKERS[1]))
    print('***************************')


def display_possible_positions():
    possible_moves = range(1, 10)
    print('Please select your next move position number from the table:')
    display(possible_moves)
    print('***************************')


def change_player(player_no):
    return PLAYER_NO[0] if player_no == PLAYER_NO[1] else PLAYER_NO[1]


def play(player_no, game_table):
    next_move = get_move(player_no, game_table)
    return move(game_table, next_move)


def get_move(player_no, game_table):
    position = get_position(player_no, game_table)
    marker = get_marker(player_no)
    return position, marker


def get_marker(player_no):
    while True:
        item = input('Player{} please enter your next marker'.format(player_no))
        if is_proper_marker(item):
            break
        else:
            display_possible_markers()
    return item


def get_position(player_no, game_table):
    while True:
        try:
            position = int(input('Player{} please enter your next marker position'.format(player_no)))
            if is_proper_position(position, game_table):
                break
            else:
                display_possible_positions()
        except ValueError:
            display_possible_positions()
    return position


def is_proper_position(position, game_table):
    for i in range(1, 10):
        if i == position and game_table[i - 1] == DEFAULT_PLACEHOLDER:
            return True
    return False


def is_proper_marker(item):
    return True if item in POSSIBLE_MARKERS else False


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
        if place == DEFAULT_PLACEHOLDER:
            return False
    return True


def is_column_match(game_table):
    for i in range(0, 3):
        if game_table[i] == game_table[i + 3] == game_table[i + 6] and game_table[i + 6] != DEFAULT_PLACEHOLDER:
            return True
    return False


def is_row_match(game_table):
    row_number = [0, 3, 6]
    for i in row_number:
        if game_table[i] == game_table[i + 1] == game_table[i + 2] and game_table[i + 2] != DEFAULT_PLACEHOLDER:
            return True
    return False


def is_cross_match(game_table):
    if game_table[0] == game_table[4] == game_table[8] and game_table[8] != DEFAULT_PLACEHOLDER:
        return True
    if game_table[2] == game_table[4] == game_table[6] and game_table[6] != DEFAULT_PLACEHOLDER:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
