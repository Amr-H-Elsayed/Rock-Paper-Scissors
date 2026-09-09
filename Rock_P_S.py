import random

def play():
    user = input("Choose:\n'R' for Rock, 'P' for Paper, 'S' for Scissors\n").upper()
    computer = random.choice(['R', 'P', 'S'])
    print("Computer Chose " + computer)

    if user == computer:
        return "It's a Tie"
    #else
    return "You Lost!"

    # r>s, s>p, p>r
    if is_win(user, computer):
        return 'You won!'

def is_win(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'P'):
        return True

print(play())