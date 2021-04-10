import API

# manually change teams here
team1 = 1274
team2 = 1275

# create game - last two arguments (board size and target) can be excluded for default 12, 6
game = API.create_game(team1, team2, 6, 3)
print(game)
