gameTable = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
possibleMoves = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def play(player):
    next_move = get_move(player)
    move(next_move[0], next_move[1])


def get_move(player_no):
    position = get_position(player_no)
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


def get_position(player_no):
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
    merged_moves = [item for innerlist in possibleMoves for item in innerlist]
    for i in merged_moves:
        if i == position:
            return True
    return False


def is_proper_item(item):
    if item == 'X' or item == 'O':
        return True
    else:
        return False


def move(position, item):
    index = 1
    for i, row in enumerate(gameTable):
        for j, col in enumerate(row):
            if index == position:
                gameTable[i][j] = item
                possibleMoves[i][j] = ' '
            index += 1


def display(table):
    for row in table:
        formatted_row = '| '
        for col in row:
            formatted_row += str(col) + ' | '
        print(formatted_row)


def is_finished():
    for i in range(3):
        if gameTable[i][0] == gameTable[i][1] and gameTable[i][1] == gameTable[i][2] and gameTable[i][0] != ' ':
            return True
        if gameTable[0][i] == gameTable[1][i] and gameTable[1][i] == gameTable[2][i] and gameTable[0][i] != ' ':
            return True
    if gameTable[0][0] == gameTable[1][1] and gameTable[2][2] == gameTable[1][1] and gameTable[0][0] != ' ':
        return True
    if gameTable[0][2] == gameTable[1][1] and gameTable[2][2] == gameTable[2][0] and gameTable[2][0] != ' ':
        return True
    return False


def start():
    display_welcome_message()
    player = 1
    while not is_finished():
        display(gameTable)
        play(player)
        player = change_player(player)
    print('Game is Finished!')
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


def change_player(player):
    if player == 2:
        return 1
    else:
        return 2


start()