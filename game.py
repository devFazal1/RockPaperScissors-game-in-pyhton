import random

def get_choices() :
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices


def check_win(player, computer):
    if player == computer:
     return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
          return "Rock smashes scissors! You win!"
        else: 
             return "paper covers rock! You lose."
    elif player == "paper":
        if computer == "scissors":
            return "scissors cut paper! You lose."
        else:
            return "paper covers rock. You win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "scissor cut paper. You win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(choices)
print(result)
