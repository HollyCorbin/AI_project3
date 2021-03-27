# class for tic tac toe game
class TTT:
    def __init__(self, gameId, board_size = 12, target = 6):
        self.gameId = gameId
        self.board_size = board_size
        self.target = target
        self.player = 'X'
        self.opponent = 'O'
        self.num_moves = 0
        self.Plist = [] # list of moves by main player
        self.Olist = [] # list of moves by opponent
        
        # self.board is used for keeping track of future moves with minimax
        self.board = [['-' for i in range(self.board_size)] for j in range(self.board_size)]
        
    # print my board
    def print_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                print(self.board[row][col], end=' ')
            print()
            
    # add move to my board
    def move(self, agent, row, col):
        self.board[row][col] = self.player
        if agent == self.player:
            self.Plist.append((row, col))
        else:
            self.Olist.append((row, col))
        self.num_moves += 1
        
    # remove move from my board
    def remove(self, agent, row, col):
        self.board[row][col] = '-'
        if agent == self.player:
            self.Plist.remove((row, col))
        else:
            self.Olist.remove((row, col))
        self.num_moves -= 1
    
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
    # finds if there is a win given moves in list
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
    
    # evaluation function calculates apporoximate value of game state
    # returns value between -1 and 1
    def evaluation(self):
        num_winning_linesP = 0
        num_winning_linesO = 0
        
        # create sets of rows and cols in which a move has been made
        rowsP = set()
        colsP = set()
        rowsO = set()
        colsO = set()
        for (row, col) in self.Plist:
            rowsP.add(row)
            colsP.add(col)
        for (row, col) in self.Plist:
            rowsP.add(row)
            colsP.add(col)
            
        # count number of unobstructed lines player occurs in
        for row in rowsP:
            # rows
            if row in rowsO: # don't add rows that are blocked by opponent
                continue
            else:
                num_winning_linesP += 1
            
            # diagonals
            blocked = False
            for t in range(self.target):
                if (row + t, col + t) in self.Olist:
                    blocked = True; break
            if not blocked:
                num_winning_linesP += 1
                
            blocked = False
            for t in range(self.target):
                if (row + t, col - t) in self.Olist:
                    blocked = True; break
            if not blocked:
                num_winning_linesP += 1
        
        # columns       
        for col in colsP:
            if col in colsO:
                continue
            else:
                num_winning_linesP += 1
        
        # number of rows, columns, and diagonals that could make a win
        # board_size # of rows and columns + 1 diagonal each way + more diagonals if target is smaller than board
        num_possible = self.board_size * 2 + 1 + 2 * (self.board_size-self.target)
        
        # divide by number of possible lines so that return is between -1 and 1
        num_winning_linesP = num_winning_linesP / num_possible
        num_winning_linesO = num_winning_linesO / num_possible
        
        return num_winning_linesP - num_winning_linesO