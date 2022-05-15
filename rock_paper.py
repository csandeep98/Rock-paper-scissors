import random

def play():
    user = input('Choose one of the following options,r for rock, p for paper, and s for scissors => ')
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'

    if is_win(user,computer):
        return 'You won'

    return 'you lost'

def is_win(user,computer):
    if(user == 'r' and computer == 's') or (user == 's' and computer =='p') or (user == 'p' and computer =='r'):
        return True

print(play())