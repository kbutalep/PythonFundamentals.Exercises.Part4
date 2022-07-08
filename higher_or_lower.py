from random import randrange


def get_user_input():
    print("Pick a number between 0 and 10\n")
    user_number = input()
    return int(user_number)

def random_number():
    ran_num = randrange(1, 11)
    return int(ran_num)

def higher_or_lower(x, y):
    while(x != y):
        if (x > y):
            print("Your number is too high. Please guess again")
            x = int(input())
            continue
        elif (x < y):
            print("Your number is too low. Please guess again")
            x = int(input())
            continue
        elif (x == y):
            print("you guessed the number")
    print("Your number is " + str(x))
    print("The random number was " + str(y))

higher_or_lower(get_user_input(), random_number())



