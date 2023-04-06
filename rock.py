#Rock, Paper, Scissors
#Passed down from the ancient Chinese Han dynasty,the game
#shoushiling is now better known as Rock, Paper, Scissors.
#This code implements a version of the game that is you against
#the computer.

# Here were doing some setup by importing the random module
# and setting up the winner variable.
import random

winner = ''

# The computer randomly chooses rock, paper, scissors by
# generating a random number from 0 to 2 and then mapping that
# to a corresponding string.

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

# Get the user's choice with a simple input statement.

user_choice = ''
while (user_choice != 'rock' and
       user_choice != 'paper' and
       user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')

# Here's our game logic, which checks to see if the computer wins
# (or not), and makes the appropriate change to the winner variable.

if computer_choice == user_choice:
    winner = 'Tie'

elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

# Here we announce the game was a tie, or the winner along
# with the computer's choice.

if winner == 'Tie':
    print ('We both chose', computer_choice + ', play again.')
else:
    print (winner, 'won. The computer chose', computer_choice + '.')


