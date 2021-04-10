from API import *
from TTT import TTT

def play(game, gameId, teamId):
    player = 'O'
    opponent = 'X'
    
    # if there is already value in board map, opponent made first move
    board_map = get_board_map(gameId)
    if board_map:
        # switch X/O values
        player = 'X'
        opponent = 'O'
        
        # add move to my board
        (row,col) = get_moves(gameId)
        game.move(opponent, row, col)
    
    turn = player
    game.player = player
    game.opponent = opponent
    while True:
        
        # wait until opponent makes a move
        while turn == opponent:
            board_map = get_board_map(gameId)
            if len(board_map) > game.num_moves:
                turn = player # switch palyers
                (row,col) = get_moves(gameId) # add move to my board
                game.move(opponent, row, col)
                get_board_string(gameId) # print board just to see moves as they happen
                
                # check for end of game
                terminal = game.end_game()
                if terminal != 2: # state is a terminal node
                    return (terminal, None, None)
        
        (value, row, col) = minimax.value(game, player) # call minimax to get best move
        make_move(gameId, teamId, row, col) # make move on API
        game.move(player, row, col) # make move on my board
        get_board_string(gameId) #print board
        turn = opponent # switch players
        
        
        # check for end of game
        terminal = game.end_game()
        if terminal != 2: # state is a terminal node
            return (terminal, None, None)
        


# execution starts here
teamId = 1275
gameId = input('game Id: ')
board_size = 12
target = 6

game = TTT(board size, target)
play(game, gameId, teamId)