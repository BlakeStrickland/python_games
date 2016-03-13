import random
secret_num = random.randint(1,10)

def play_again():
    play = input("Do you want to play again? Y/n: ")
    if play.lower() != 'n':
        play_game()
    else:
        print("K Bye")

def play_game():
    guesses = []
    while len(guesses) < 5:
        try:
            guess = int(input('Guess a number from 1 to 10: '))
        except ValueError:
            print('Not a valid int')
        else:
            if guess == secret_num:
                print("You got it! The secret number was {}".format(secret_num))
                break
            elif guess > secret_num:
                print("Your number was too high!")
                print("You have {} guess(es) remaining".format(5 - len(guesses)-1))
                guesses.append(guess)
                continue
            elif guess < secret_num:
                print("Your number was too low!")
                print("You have {} guess(es) remaining".format(5 - len(guesses)-1))
                guesses.append(guess)
                continue
    else:
        print("Too bad, the number was {}".format(secret_num))
        play = input("Do you want to play again? Y/n: ")
        if play.lower() != 'n':
            guesses = []
            play_game()
        else:
            print("Peace")



play_game()
