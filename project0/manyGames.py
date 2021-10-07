# Many Games
# Modify Game Preferences so your user can add as many games as they like.
games = ['minecraft','fifa','head soccer','monopoly']

print("i like to play:")
print(*games, sep= ", ")

choice = 'y'
while choice == 'y':
    userGame = input("what game do you like? ")
    games.append(userGame)
    choice = input("awesome, would you like to enter another game? (y/n)")

print("we like to play:")
print(*games, sep= ", ")