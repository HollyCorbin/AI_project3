from copy import deepcopy

# runs minimax algorithm
def value(game, agent, alpha=float('-inf'), beta=float('inf'), depth = 0):
    terminal = game.end_game()
    if terminal != 2: # state is a terminal node
        return (terminal, None, None)
    
    # stop at depth 3 to make game fater
    if depth > 3:
        # use evaluation function to get value of move
        v = game.evaluation()
        return (v, None, None)
    
    # max
    if agent==game.player:
        v = float('-inf')
        
        # get all successor moves in order of those that will be most useful
        successors = get_successors(game)
        
        for (row, col) in successors:
            # copy game state and make move on copy
            child = deepcopy(game)
            child.move(game.player, row, col)
            # get value of new game state
            v_successor, row_max, col_max = value(child, game.opponent, alpha, beta, depth+1)
            
            # update best valued move
            if v_successor > v:
                v = v_successor
                r = row
                c = col
            
            # alpha beta pruning
            alpha = max(alpha, v)
            if alpha >= beta:
                break
            
        # return value, row, column of best move 
        return (v, r, c)
    
    # min
    else:
        v = ('inf')
        
        # get all successor moves in order of those that will be most useful
        successors = get_successors(game)
        
        for (row, col) in successors:
            # copy game state and make move on copy
            child = deepcopy(game)
            child.move(game.player, row, col)
            # get value of new game state
            v_successor, row_min, col_min = value(child, game.player, alpha, beta, depth+1)
            
            # update best valued move
            if v_successor < v:
                v = v_successor
                r = row
                c = col
                
            # alpha beta pruning
            beta = min(beta, v)
            if beta <= alpha:
                break
            
        # return value, row, column of best move 
        return (v, r, c)
    

# puts moves that are close to already played moves at the front of successor list
# makes pruning more likely
def get_successors(game):
    successors = game.open_spaces # successors are updated every move
    
    for (row,col) in game.Plist:
        if (row,col+1) in successors:
            successors.insert(0, successors.pop(successors.index((row,col+1))))
        if (row,col-1) in successors:
            successors.insert(0, successors.pop(successors.index((row,col-1))))
        if (row+1,col) in successors:
            successors.insert(0, successors.pop(successors.index((row+1,col))))
        if (row-1,col) in successors:
            successors.insert(0, successors.pop(successors.index((row-1,col))))
        if (row+1,col+1) in successors:
            successors.insert(0, successors.pop(successors.index((row+1,col+1))))
        if (row+1,col-1) in successors:
            successors.insert(0, successors.pop(successors.index((row+1,col-1))))
        if (row-1,col+1) in successors:
            successors.insert(0, successors.pop(successors.index((row-1,col+1))))
        if (row-1,col-1) in successors:
            successors.insert(0, successors.pop(successors.index((row-1,col-1))))
    for (row,col) in game.Olist:
        if (row,col+1) in successors:
            successors.insert(0, successors.pop(successors.index((row,col+1))))
        if (row,col-1) in successors:
            successors.insert(0, successors.pop(successors.index((row,col-1))))
        if (row+1,col) in successors:
            successors.insert(0, successors.pop(successors.index((row+1,col))))
        if (row-1,col) in successors:
            successors.insert(0, successors.pop(successors.index((row-1,col))))
        if (row+1,col+1) in successors:
            successors.insert(0, successors.pop(successors.index((row+1,col+1))))
        if (row+1,col-1) in successors:
            successors.insert(0, successors.pop(successors.index((row+1,col-1))))
        if (row-1,col+1) in successors:
            successors.insert(0, successors.pop(successors.index((row-1,col+1))))
        if (row-1,col-1) in successors:
            successors.insert(0, successors.pop(successors.index((row-1,col-1))))
    return successors
    
