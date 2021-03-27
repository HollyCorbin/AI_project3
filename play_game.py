from API import *
from TTT import *
import minimax

def play(game, team):
    player = 'O'
    opponent = 'X'
    
    # if there is already value in board map, opponent made first move
    board_map = get_board_map(game.gameId)
    if board_map:
        # switch X/O values
        player = 'X'
        opponent = 'O'
        
        # add move to my board
        move = get_moves(game.gameId)
        game.move(opponent, move[0], move[1])
    
    turn = player
    game.player = player
    game.opponent = opponent
    while True:
        
        # wait until opponent makes a move
        while turn == opponent:
            board_map = get_board_map(game.gameId)
            if len(board_map) > game.num_moves:
                turn = player # switch palyers
                move = get_moves(game.gameId) # add move to my board
                game.move(opponent,move[0],move[1])
                get_board_string(game.gameId) # print board just to see moves as they happen
                
                # check for end of game
                terminal = game.end_game()
                if terminal != 2: # state is a terminal node
                    return (terminal, None, None)
        
        # call minimax to get best move
        (value, row, col) = minimax.value(game, player)
        make_move(game.gameId, teamId, row, col) # make move on API
        game.move(player, row, col) # make move on my board
        get_board_string(game.gameId) #print board
        turn = opponent # switch players
        
        # check for end of game
        terminal = game.end_game()
        if terminal != 2: # state is a terminal node
            return (terminal, None, None)
        



# execution starts here
teamId = 1275
gameId = input('game Id: ')

game = TTT(gameId, 12, 6) # TTT(gameId, board size, target)
play(game, teamId)
