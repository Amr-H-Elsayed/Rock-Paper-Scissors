import random

def play():
    user = input("Choose:\n'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a Tie"
    #else
    return "You Lost!"

    # r>s, s>p, p>r
    if is_win(user, computer):
        return 'You won!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())