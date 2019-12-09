import random
import time
global board

# For code style i use PEP-8

board = [' ' for x in range(10)]


def plog_in(input, spot):
    """ To insert the letter
    in the board
    """
    board[spot] = input


def free_space(spot):
    # To  check if the position
    return board[spot] == ' '


def play_again():
    ask = input('Do you want to play a again?( Y or N )')
    if ask == 'Y':
        print('~~~~')
        board = [' ' for x in range(10)]
        main()
    else:
        exit()


def print_board(board):
    # To print the board the beautiful form
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def is_winner(bo, le):
    """ To check if we have a winner
    in the board.
    le stand for letter.
    bo stand for board.
    """
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
           (bo[4] == le and bo[5] == le and bo[6] == le) or (
            bo[1] == le and bo[2] == le and bo[3] == le) or \
           (bo[1] == le and bo[4] == le and bo[7] == le) or (
            bo[2] == le and bo[5] == le and bo[8] == le) or (
            bo[3] == le and bo[6] == le and bo[9] == le) or (
            bo[1] == le and bo[5] == le and bo[9] == le) or \
           (bo[3] == le and bo[5] == le and bo[7] == le)


def cls_screen():
    """ To clear the Console,
    using  \033 -ASCII escape character!
           [H  - move the cursor to the home position!
           [J  -erases the screen from the current line down
           to the bottom of the screen.
    """
    print("\033[H\033[J")
    print("\033[H\033[J")
    print("\033[H\033[J")
    print("\033[H\033[J")
    return


def player_move():
    # To get the Player move.
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        time.sleep(0.5)
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_space(move):
                    run = False
                    plog_in('X', move)
                else:
                    print('Sorry, this space is occupied!')
                    time.sleep(0.5)
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def comp_move():
    """ To get the computer move then use
    an (AI) algorithm to let
    the computer win!.
    this part it has been taking
    from an open source!
    """
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edgesOpen = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = select_random(edgesOpen)

    return move


def select_random(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def is_board_full(board):
    """ To check if we have
    more then 1 position in
    the board then  it not full
    """
    if board.count(' ') > 1:
        return False
    else:
        return True


def start():
    info = """ Welcome to (X & O)game !>>
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  #Game instruction
      1-The Player well take a X letter in the Game!
      2-The computer well used a O letter!
      **Hint >>The computer have an (AI) so Work Hard to win (^-^)!
      """
    print(info)
    return


def main():
    start()
    global board
    board = [' ' for x in range(10)]
    print_board(board)
    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('Sorry, O\'s won this time!')
            time.sleep(0.4)
            cls_screen()
            play_again()
        if not (is_winner(board, 'X')):
            move = comp_move()
            if move == 0:
                print('Tie Game!')
                cls_screen()
                play_again()
            else:
                plog_in('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                time.sleep(0.4)
                print_board(board)
        else:
            print('X\'s won this time!>> i am proud of you !')
            cls_screen()
            play_again()
    if is_board_full(board):
        print('Tie Game!')
        cls_screen()
        play_again()


main()
