import random
# create a str with 3 numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
guess_numbers_str = ''.join(str(random.choice(numbers)) for _ in range(3))
# take users guess
user_guess = input("Guess 3 numbers:  ")

# need to check for each digit in guess
def check_guess(guess, answer):
    if guess == answer:
        return "Winner"

    shuffel_answer = random.sample(answer, len(answer))
    clues = []
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            clues.append("Fermi")
        elif guess[i] in shuffel_answer:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else: 
        return ' '.join(clues)
def gameloop():
    clues = check_guess(user_guess, guess_numbers_str)
    print(clues)
# TODO: create game loop that tracks guesses
gameloop()



