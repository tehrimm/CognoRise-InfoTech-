import random

def is_win(player, opponent):
    # Winning conditions: r > s, s > p, p > r
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

def play_round():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"You and the computer both chose {computer}. It's a tie!")
        return 0, 0  # No points awarded
    elif is_win(user, computer):
        print(f"You chose {user} and the computer chose {computer}. You won this round!")
        return 1, 0  # Player wins
    else:
        print(f"You chose {user} and the computer chose {computer}. You lost this round.")
        return 0, 1  # Computer wins

def play_game():
    rounds = int(input("How many rounds would you like to play? "))
    player_wins = 0
    computer_wins = 0

    for _ in range(rounds):
        player_score, computer_score = play_round()
        player_wins += player_score
        computer_wins += computer_score

        print(f"Scoreboard: You {player_wins} - {computer_wins} Computer\n")

    if player_wins > computer_wins:
        print(f"You have won the best of {rounds} games! What a champ :D")
    elif computer_wins > player_wins:
        print(f"Unfortunately, the computer has won the best of {rounds} games. Better luck next time!")
    else:
        print(f"It's a tie overall with both winning {player_wins} rounds each!")

play_game()
