"""A number-guessing game."""
import random
#greet player
print("Hello, player! Welcome to our guessing game!")

#get player name
player_name=input("What is your Name? ")


def request_range():
    print("Tell us the range you want to guess! Range must have 40 to 100 numbers in it")

    min_range = 40
    max_range = 100


    while True:
        start=int(input("Give a number to start your range of guesses. "))
        end=int(input("Give a number to end your range of guesses. "))
        calc_range = end - start + 1

        if calc_range < min_range:
            print("You don't have enough numbers in your range.\n")

        elif calc_range > max_range:
            print("You have too many numbers in your range!")

        else: 
            break

    return (start,end)


def game():
#choose random number between 1 and 100
    start,end=request_range()

    secret_number = random.randint(start,end+1)
    print(secret_number)

    guesses=0
    win = True

    while guesses<5:
        #add a loop to check for valid input
        while True:
            user_guess=input("Choose a random number between {} and {}: ".format(start,end))

            # if not user_guess.isdigit():
            #     print("Please enter an integer.")
            #     print()
            try:
                user_guess = int(user_guess)

                if int(user_guess)<start or int(user_guess)>end:
                    print("I said a number BETWEEN {} and {}!!".format(start,end))
                    print()
                else:
                    break

            except ValueError:
                print("Please enter an integer")
                print()

        guesses+=1

        if user_guess != secret_number:
            if guesses == 5:
                print("You've exceeded the number of allowed guesses. You lose!")
                print("The secret number was {}\n".format(secret_number))
                win = False

            elif user_guess < secret_number:
                print("Your guess is too low, try again.")
                print()

            elif user_guess > secret_number:
                print("Your guess is too high, try again")
                print()

        elif user_guess == secret_number:
            print("Well done, {}! You found my number in {} tries!".format(player_name,guesses))
            break

    return (win, guesses)

def play_again():
    best_score = None
    wins = 0
    games_played = 0
    #play game on a loop
    while True:
        win, guesses = game()

        games_played += 1
        if win == True:
            wins += 1
        # track the best score only if a win
        if win > 0 and best_score == None:
            best_score = guesses
        elif win > 0 and guesses < best_score:
            best_score = guesses
        # ask to play again if they win
        play_again=input("Would you like to play again? Y/N \n").upper()

        if play_again.startswith("N"):
            print("Thank you for playing!")
            if wins == 0:
                print("You lost all {} of your games".format(games_played))
            else:
                print("Your best score was {} guesses and you won {} out of {} games.".format(best_score, wins, games_played))
            break




play_again()
