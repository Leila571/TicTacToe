'''
10/1/2020
Leila Lopez Marks
Tic Tac Toe Board
'''

# welcome message
# draw board
# choose number of players 0, 2
# choose X or O
# random pick who goes first
# Place first entry on board
# Gameplay
# check for winning or tie condition
# Outcome message
# Ascii art
# Would you like to play again message if y refresh if n exit

vertical = [' | | ']
horizontal = [' - - - ']

def board():
    for i in range(3):
        print(vertical[0])
        if i < 2:
            print(horizontal[0])


print("Welcome to Tic Tac Toe")
num_of_players = input("Choose the number of players. Valid inputs are: 0,1, or 2")
print("You have chosen ", num_of_players, "players")

x_or_o = input("Chose X's or O's: ").upper() # Input for X or O's
if x_or_o == 'X':
    print(f"Player 1 is X's and player 2 is O's")
else:
    print("Player 1 is O's and player 2 is X's")

board()