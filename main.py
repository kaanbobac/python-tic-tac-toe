gameTable = [' ']*10
possibleMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_no = 1

def play():
    next_move = get_move()
    move(next_move[0], next_move[1])


def get_move():
    position = get_position()
    item = get_item()
    return position, item


def get_item():
    while True:
        item = input('Player{} please enter your next item'.format(player_no))
        if is_proper_item(item):
            break
        else:
            display_possible_items()
    return item


def get_position():
    while True:
        try:
            position = int(input('Player{} please enter your next item position'.format(player_no)))
            if is_proper_position(position):
                break
            else:
                display_possible_moves()
        except ValueError:
            display_possible_moves()
    return position


def is_proper_position(position):
    for i in possibleMoves:
        if i == position:
            return True
    return False


def is_proper_item(item):
    if item == 'X' or item == 'O':
        return True
    else:
        return False


def move(position, item):
    gameTable[position - 1] = item
    possibleMoves[position - 1] = ''


def display(table):
    row = ''
    for index, value in enumerate(table):
        row += str(value) + ' | '
        if (index + 1) % 3 == 0:
            print(row)
            row = ''


def is_finished():
    return is_board_full() or is_column_match() or is_row_match() or is_cross_match()


def is_board_full():
    for move in possibleMoves:
        if move != '':
            return False
    return True
def is_column_match():
    for i in range(0, 3):
        if gameTable[i] == gameTable[i + 3] and gameTable[i + 3] == gameTable[i + 6] and gameTable[i + 6] != ' ':
            return True
    return False


def is_row_match():
    row_number = [0, 3, 6]
    for i in row_number:
        if gameTable[i] == gameTable[i + 1] and gameTable[i + 1] == gameTable[i + 2] and gameTable[i + 2] != ' ':
            return True
    return False


def is_cross_match():
    if gameTable[0] == gameTable[4] and gameTable[4] == gameTable[8] and gameTable[8] != ' ':
        return True
    if gameTable[2] == gameTable[4] and gameTable[4] == gameTable[6] and gameTable[6] != ' ':
        return True
    else:
        return False


def start():
    display_welcome_message()
    while not is_finished():
        display(gameTable)
        play()
        change_player()
    print('Game is Over!')
    print('---This is final result----')
    display(gameTable)


def display_welcome_message():
    print('***************************')
    print('Welcome to TIC TAC TOE Game')
    print('***************************')
    display_possible_moves()


def display_possible_moves():
    display_possible_items()
    display(possibleMoves)
    print('***************************')


def display_possible_items():
    print('Please make your X or O moves by the following position numbers')


def change_player():
    if player_no == 2:
        return 1
    else:
        return 2


start()
