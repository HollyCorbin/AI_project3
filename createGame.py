import API

# manually change teams here
team1 = 1275
team2 = 1274

# create game - last two arguments (board size and target) can be excluded for default 12, 6
game = API.create_game(team1, team2, 12, 6)
print(game)
