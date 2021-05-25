import random

lives = 3
times_won = 0
RPS = ['r', 'p', 's']


def play():
    user = input(
        "Whats your choice? \n 'r' for rock , \n 'p' for paper, \n 's' for scissors: \n")
    computer = random.choice(RPS)
    if user not in RPS:
        return "Invalid choice, pick again. \n 'r' for rock , \n 'p' for paper, \n 's' for scissors: \n"

    win_result = is_win(user, computer)

    if win_result == True:
        game_result = f'>> Rock, Paper, Scissors! \nYou Won!, Computer chose {computer} \n {user} beats {computer}'

    elif win_result == 'tie':
        game_result = f">> Tie. You both chose {computer}"
    else:
        game_result = f'>> Rock, Paper, Scissors! \nYou lost :( Computer chose {computer} \n {computer} beats {user}'

    return game_result


def is_win(player, opponent):
    global lives
    global times_won

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        times_won += 1
        return True
    elif (opponent == 'r' and player == 's') or (opponent == 's' and player == 'p') or (opponent == 'p' and player == 'r'):
        lives -= 1
        times_won = 0
        return False
    elif opponent == player:
        return "tie"

# we need to access the variables 'lives' and 'times_won' from the top of the page - use solution from global article

# if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        #times_won += 1
        # return True

# elif (opponent == 'r' and player == 's') or (opponent == 's' and player == 'p') or (opponent == 'p' and player == 'r'):
        #lives -= 1
        #times_won = 0
        # return False

        # elif opponent == player:
        # return "tie"

# __________________________________________________________________
# Introduction section. it comes last beacuse its where we call play()- you only call a fucntion after its been made / at the bottom of page


want_to_play = input(
    "Welcome to the Rock, Paper, Scissors Tournament!\n Do you want to play? [yes/no]: ")

if want_to_play == 'yes':
    name = input("What is your name?: ")
    print(f"welcome {name}")

    # - NOTE:
    # Write the formatted version if you remember how

    print("Win against the computer three times in a row to win the tournament\n you have 3 lives, if you lose a round, you lose a life\n if there is a tie you will not lose a life.\n Good luck!")
    while lives > 0 and times_won < 3:
        print(play())
        print(f"lives remaining: {lives}")
        print(f"times won in a row: {times_won}")

    if times_won == 3:
        print("Congratulations! You've won!")
    if lives == 0:
        print("No more lives, you've lost!")

elif want_to_play == 'no':
    print("Too bad, maybe next time!")
else:
    print("Invalid choice, choose yes or no")

    # while loops starts here. the condition for the while loop:

    # whilst lives is greater than 0(so, 1, 2, 3) AND times_won < 3(so, 0,1,2) this condition confused me a bit but it works and ill try explain

    # while *condition*:
    # call the play function
    # each round we want to show how many lives are remaining
    # each round we want to show how many times won in a row
    # change or fill-out whats missing
    # print(?"lives remaining: {}")
    # print(?"Times won in a row: {}")

    # if statement for when times_won == 3
    # if statement for when lives == 0

    # code for if the user does not want_to_play

    # code for when user inputs anything other than yes or no when asked to play

    # DONEEEE
