import random

def get_choices():
    options = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ")
    computer_choice = random.choice(options)
    
    choices = {'user_choice' : user_choice, 'computer_choice': computer_choice}
    return choices

def check_win(player, computer):
    if player == computer:
        print(f"Computer choice: {computer} | It's a tie")
    elif player == 'rock':
        if computer == 'scissors':
            print(f"Computer choice: {computer} | Rock break scissor. You Win")
        else:
            print(f"Computer choice: {computer} |  Paper covers Rock. You Lose")
    elif player == 'scissor':
        if computer == 'rock':
            print(f"Computer choice: {computer} | Rock beats scissors. You lost")
        else:
            print(f"Computer choice: {computer} | Scissor cuts paper. You win")
    elif player == 'paper':
        if computer == 'Rock':
            print(f"Computer choice: {computer} | Paper covers rock. You win")
        else:
            print(f"Computer choice: {computer} | Scissor cuts paper. You Lost")
    
    
choices = get_choices()
result = check_win(choices['user_choice'], choices['computer_choice'])
    
