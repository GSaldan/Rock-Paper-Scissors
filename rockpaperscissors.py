import random
# instructions: choose rock paper or scissors and the computer will pick randomly between one of 
# the options and see who wins


def game():
    # player and computer choose what to play
    computer_options = ['rock', 'paper', 'scissors']
    player_choice = input('Write your choice, rock, paper or scissors: ')
    computer_choice = random.choice(computer_options)
    dict_ = {'player': player_choice, 'computer': computer_choice}
    return dict_


def check_win(player, computer):
    # combine the player and computer choice and compare to see who wins
    print(f'you played >{player}< and the computer played >{computer}<')
    if player == computer:
        return 'TIE!'
    elif player == 'rock':
        if computer == 'paper':
            return 'You lose.'
        else:
            return 'You win!'
    elif player == 'paper':
        if computer == 'scissors':
            return 'You lose.'
        else:
            return 'You win!'
    elif player == 'scissors':
        if computer == 'rock':
            return 'You lose.'
        else:
            return 'You win!'


choices = game()
result = check_win(choices['player'], choices['computer'])
print(result)