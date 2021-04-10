from TTT import TTT
import minimax

def play(game):
    game.print_board()
    print()
    player = 'X'
    while True:
        if player == 'O':
            (row,col) = input('move: ').split(',')
            row = int(row)
            col = int(col)
            game.move('O', row, col)
            game.print_board()
            print()
        
            terminal = game.end_game()
            if terminal != 2: # state is a terminal node
                return (terminal, None, None)
        
        else:
            (v, r, c) = minimax.value(game, player)
            game.move(player, r, c)
            game.print_board()
            print()
            
            terminal = game.end_game()
            
            if terminal != 2: # state is a terminal node
                return (terminal, None, None)
        
        if player == 'X': player = 'O'
        elif player == 'O': player = 'X'
        

g = TTT(6,3)
play(g)