board_size = 3
board =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def draw_board(): #вывести доску
    print('_' * 4 * board_size)
    for i in range (board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i*3], '|', board[1+i*3],'|',board[2+i*3], '|')
        print('_' * 4 * board_size)
def game_step(index, char): #сделать ход
    if (index > 9 or index < 1 or board[index-1] in ('x', 'o')):
        return False
    board[index-1] = char
    return True
def check_win():
    win = False
    win_comb = {
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    }
    for pos in win_comb:
        if (board[pos[0]]==board[pos[1]] and board[pos[1]]== board[pos[2]]):
            win = board[pos[0]]
    return win
def start_game():
    player = 'x'
    step = 1
    draw_board()
    while (step < 10) and (check_win() == False):
        index = input('ходит игрок : '  + player + ' Введите номер поля')
        if (game_step(int(index), player)):
            print('удачный ход')
            if (player == 'x'):
                player = 'o'
            else:
                player = 'x'
            draw_board()
        else:
            print('Неверный ход')
        step+=1
    print('Выйграл' + check_win())
print('Крестики нолики')
start_game()