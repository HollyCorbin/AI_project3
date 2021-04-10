https://github.com/HollyCorbin/AI_project3.git

create_game.py will create a game in the API. TeamIds have to be manually entered into into the file. Game size and target can also be entered in the file or it will use the default 12, 6. It prints out the game Id.

play_game.py will run the game, first asking for user input for the game ID and then automatically making all moves in the API.

play_game.py: Alternates between players. On opponents turn, waits for the API board to change then switches to my turn. On my turn, gets best move by calling minimax.py then makes the move. Checks for end-of-game after every move.

minimax.py: Uses minimax search with alpha-beta pruning to get the values of each branch of the game tree and returns the best-valued move. Orders choice of next branch to expand by a successor function that puts moves that are more likely to win the game as the first choices. When the search tree reaches its maximum depth, it uses an evaluation function to determine the approximate value of a game state based on the number of moves in a row for each player.

TTT.py: Holds structure for tic-tac-toe game and associated functions like evaluation function and function to determine terminal nodes.

API.py: Holds all operations for the API.
