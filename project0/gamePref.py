# Game Preferences
# Make a list that includes 3 or 4 games that you like to play.
# Print a statement that tells the user what games you like.
# Ask the user to tell you a game they like, and store the game in a variable such as new_game.
# Add the user's game to your list.
# Print a new statement that lists all of the games that we like to play (we means you and your user).
games = ['minecraft','fifa','head soccer','monopoly']

print("i like to play:")
print(*games, sep= ", ")
userGame = input("what game do you like? ")
games.append(userGame)
print("we like to play:")
print(*games, sep= ", ")