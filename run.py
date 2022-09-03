import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Sorry, guess again. Too LOW")
        elif guess > random_number:
            print("Sorry, guess again. Too HIGH")

    print(f"Yaay, congrats. You have guessed the number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        guess = random.randint(low, high)
        feedback = input(f"I {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"Yaay, the computer guessed you number: {guess} correctly")


guess(100)
computer_guess(100)