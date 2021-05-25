import random

lives = 3
times_won = 0
RPS = ['r', 'p', 's']


def play():
    user = input(
        "Whats your choice? \n 'r' for rock , \n 'p' for paper, \n 's' for scissors: \n")
    computer = random.choice(RPS)
    if user not in RPS:
        return "Invalid choice. \n 'r' for rock , \n 'p' for paper, \n 's' for scissors: \n"

    win_result = is_win(user, computer)

    if win_result == True:
        game_result = f'>> Rock, Paper, Scissors! \nYou Won!, Computer chose {computer} \n {user} beats {computer}'

    elif win_result == "tie":
        game_result = f">> Tie. You both chose {computer}"

    # dont need 'else'
    else:
        game_result = f'>> Rock, Paper, Scissors! \nYou lost :( Computer chose {computer} \n {computer} beats {user}'

    return game_result


def is_win(player, opponent):
    global lives
    global times_won

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        times_won += 1
        return True
    # elif player == opponent:
    #     return "tie"
    elif (opponent == 'r' and player == 's') or (opponent == 's' and player == 'p') or (opponent == 'p' and player == 'r'):
        lives -= 1
        times_won = 0
        return False
    elif opponent == player:
        return "tie"


want_to_play = input(
    "Welcome to the Rock, Paper, Scissors Tournament!\n Do you want to play? [yes/no]: ")

if want_to_play == 'yes':
    name = input("What is your name?: ")
    print("welcome" + " " + name)

    print("Win against the computer three times in a row to win the tournament\n you have 3 lives, if you lose a round, you lose a life\n if there is a tie you will not lose a life.\n Good luck!")
    while lives > 0 and times_won < 3:  # soon as one is false, loop breaks
        print(play())
        print(f"lives remaining: {lives}")
        print(f"Times won in a row: {times_won}")

    if times_won == 3:
        print("CONGRATS, YOU WON!")
    if lives == 0:
        print("You ran out of lives. You lost".upper())


elif want_to_play == "no":
    print("Too bad! Maybe next time!")
else:
    print("invalid choice, choose yes or no.")
