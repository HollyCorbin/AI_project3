class TTT:
    def __init__(self, board_size = 12, target = 6):
        self.board_size = board_size
        self.target = target
        self.player = 'X'
        self.opponent = 'O'
        self.num_moves = 0
        
        # lists of all moves made by each player
        self.Plist = []
        self.Olist = []
        
        # empty board to start
        self.board = [['-' for i in range(self.board_size)] for j in range(self.board_size)]
        
        # keeps track of number of moves in a row for each length
        self.linesP = [0 for i in range(self.target)]
        self.linesO = [0 for i in range(self.target)]
        
        # for getting successor nodes in minimax
        self.open_spaces = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.open_spaces.append((i,j))
                
    # add move to my board
    def move(self, agent, row, col):
        self.update_lines(agent, row, col) # update number of lines of each length for evaluation
        self.board[row][col] = agent # update my board
        
        # update lists of moves
        if agent == self.player:
            self.Plist.append((row, col))
        else:
            self.Olist.append((row, col))
        
        self.num_moves += 1
        self.open_spaces.remove((row,col)) # remove this move from possible successors
     
    # keeps track of the number of moves in each length
    # for example 2 separate moves of player and 1 move of length 2 --> Plines = [2,1,...]
    # used for evaluation function
    def update_lines(self, agent, row, col):
        # lines along rows
        t = 1
        start = col
        end = col
        while col-t >=0 and self.board[row][col-t] == agent:
            start = col-t
            t += 1
        t = 1
        while col+t < self.board_size and self.board[row][col+t] == agent:
            end = col+t
            t += 1
        length = end - start + 1
        length = min(length, self.target)
        if agent == self.player:
            self.linesP[length-1] += 1
        else:
            self.linesO[length-1] += 1
            
        # lines down columns
        t = 1
        start = row
        end = row
        while row-t >=0 and self.board[row-t][col] == agent:
            start = row-t
            t += 1
        t = 1
        while row+t < self.board_size and self.board[row+t][col] == agent:
            end = row+t
            t += 1
        length = end - start + 1
        length = min(length, self.target)
        if agent == self.player:
            self.linesP[length-1] += 1
        else:
            self.linesO[length-1] += 1
            
        # diagonal down left to right
        t = 1
        start = row
        end = row
        while row-t >=0  and col-t >= 0 and self.board[row-t][col-t] == agent:
            start = row-t
            t += 1
        t = 1
        while row+t < self.board_size and col+t < self.board_size and self.board[row+t][col+t] == agent:
            end = row+t
            t += 1
        length = end - start + 1
        length = min(length, self.target)
        if agent == self.player:
            self.linesP[length-1] += 1
        else:
            self.linesO[length-1] += 1
        
        # diagonal down right to left
        t = 1
        start = row
        end = row
        while row+t < self.board_size and col-t >=0 and self.board[row+t][col-t] == agent:
            start = row-t
            t += 1
        t = 1
        while row-t >=0  and col+t < self.board_size and self.board[row-t][col+t] == agent:
            end = row+t
            t += 1
        length = end - start + 1
        length = min(length, self.target)
        if agent == self.player:
            self.linesP[length-1] += 1
        else:
            self.linesO[length-1] += 1

       
    
    # check if current state of board is a terminal node - indicates end of game
    # return 0 if game is tie
    # return 1 if player wins game
    # return -1 if opponent wins game
    # return 2 if game is not over
    def end_game(self):
        if len(self.Plist) >= self.target:
            win = self.find_wins(self.Plist) # True if a win is found with X
            if win:
                if self.player == 'X':
                    return 1
                else:
                    return -1
                
        if len(self.Olist) >= self.target:
            win = self.find_wins(self.Olist) # True if a win is found with O
            if win:
                if self.player == 'O':
                    return 1
                else:
                    return -1
                
        # tie, no empty position left on board
        tie = True
        for line in self.board:
            if '-' in line:
                tie = False; break
        if tie:
            return 0
    
        return 2
        
    
    # helper for end_game()
    # finds if there is a win given a list of moves
    # by checking that if there are target # of moves in each direction
    def find_wins(self, list):
        for i in range(len(list)):
            row = list[i][0]
            col = list[i][1]
            
            # vertical wins
            win = True
            for j in range(self.target):
                if (row,col+j) not in list:
                    win = False; break
            if win:
                return True
            
            # horizontal wins
            win = True
            for j in range(self.target):
                if (row+j,col) not in list:
                    win = False; break
            if win:
                return True
            
            # diagonal wins - down left to right
            win = True
            for j in range(self.target):
                if (row+j,col+j) not in list:
                    win = False; break
            if win:
                return True
            
            # diagonal wins - down right to left
            win = True
            for j in range(self.target):
                if (row+j,col-j) not in list:
                    win = False; break
            if win:
                return True
        
        return False
    
    
    # evaluation function calculates approximate value of game state
    # based on number of lines of each length for both players
    def evaluation(self):
        evalP = 0
        evalO = 0
        for i in range(1, self.target):
            evalP += self.linesP[i] * (i ** i)# gives more weight to longer lines
            evalO += self.linesO[i] * (i ** i)
        
        # divide so return value is between -1 and 1
        evalP = evalP / (len(self.Plist)*(self.target**self.target))
        evalO = evalO / (len(self.Olist)*(self.target**self.target))
        return evalP - evalO 
        
