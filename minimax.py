
# dispatch for minimax
def value(game, agent, alpha=float('-inf'), beta=float('inf'), depth = 0):
    
    # only need to check for terminal nodes after certain number of moves
    if game.num_moves > 2 * game.target - 1:
        terminal = game.end_game()
        if terminal != 2: # state is a terminal node
            return (terminal, None, None)
        
    # stop at depth 3 to make game fater
    if depth > 3:
        # use evaluation function to get value of move
        v = game.evaluation()
        return (v, None, None)
        
    if agent == game.player: # max
        return max_value(game, alpha, beta, depth)
    else: #min
        return min_value(game, alpha, beta, depth)

# gets max-valued move from all successor moves
def max_value(game, alpha, beta, depth):
    v = float('-inf')
    r = None
    c = None
    
    # get all successor moves in order of those that will be most useful
    successors = get_successors(game, game.opponent)
    
    for (row, col) in successors:
        game.move(game.player, row, col) # put potential move on my board
        v_successor = 0
        
        # get value of new game state
        (v_successor, min_row, min_col) = value(game, game.opponent, alpha, beta, depth+1)
        
        # update best valued move
        if v_successor > v:
            v = v_successor
            r = row
            c = col
        
        game.remove(game.player, row, col) # reset board
        
        # alpha beta pruning
        if v >= beta:
            return (v, r, c)
        alpha = max(alpha, v)
    
    # return value, row, column of best move
    return (v, r, c) 
 
# gets min-valued move from all successor moves
def min_value(game, alpha, beta, depth):
    v = float('inf')
    r = None
    c = None
    
    
    # get all successor moves in order of those that will be most useful
    successors = get_successors(game, game.opponent)
    for (row, col) in successors:
        game.move(game.opponent, row, col) # put potential move on my board
        v_successor = 0
        
        # get value of new game state
        (v_successor, max_row, max_col) = value(game, game.player, alpha, beta, depth+1)
        # update best valued move
        if v_successor < v:
            v = v_successor
            r = row
            c = col
        game.remove(game.opponent, row, col)
        
        # aplha beta pruning
        if v <= alpha:
            return (v, r, c)
        beta = max(beta, v)
    
    # return value, row, column of best move
    return (v, r, c)

# i.e. moves that are in the same row or column as already played moves
# makes pruning more likely
def get_successors(game, agent):
    successors = []
    if agent == game.player:
        for move in game.Plist:
            for i in range(game.board_size):
                # rows
                if game.board[move[0]][i] == '-' and (move[0], i) not in successors:
                    successors.append((move[0], i))
                # columns
                if game.board[i][move[1]] == '-' and (i, move[1]) not in successors:
                    successors.append((i, move[1]))
                    
    else:
        for move in game.Olist:
            for i in range(game.board_size):
                # rows
                if game.board[move[0]][i] == '-' and (move[0], i) not in successors:
                    successors.append((move[0], i))
                # columns
                if game.board[i][move[1]] == '-' and (i, move[1]) not in successors:
                    successors.append((i, move[1]))
                    
    for row in range(game.board_size):
        for col in range(game.board_size):
            if (row,col) not in successors and game.board[row][col] == '-':
                successors.append((row,col))
    return successors
