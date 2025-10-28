# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anthony Do
# Section: 217
# Assignment: Lab 9.19 Word Puzzle
# Date: 23 October 2025

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)
    print()
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")

    if is_valid_guess(get_valid_letters(puzzle), guess):
        numbers = make_numbers(puzzle, guess)
        if not check_user_guess(numbers[0], numbers[1], numbers[2], numbers[3]):
            print("Try again!")
        else: 
            print("Good job!")

    else:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")

        

def get_valid_letters(puzzle):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uniqueLetters = ""

    while len(uniqueLetters) < 10:
        for letter in puzzle:
            if letter in letters and not letter in uniqueLetters:
                uniqueLetters += letter

    return uniqueLetters

def is_valid_guess(validLetters, guess):
    guessValid = ""

    if len(guess) != 10:
        valid = False
    else:
        valid = True

    for letter in guess:
        if letter in validLetters and not letter in guessValid:
            guessValid += letter
        else:
            valid = False
    return valid

def check_user_guess(dividend, quotient, divisor, remainder):
    return dividend == quotient * divisor + remainder

def make_number(word, guess):
    conversion = ""
    dict = {}
    i = 0

    for letter in guess:
        dict.update({letter: str(i)})
        i += 1
    
    for letter in word:
        if letter in dict:
            conversion += dict[letter]

    return int(conversion)

# For given puzzle RUMORS, RUE, EAR, USA
def make_numbers(puzzle, guess):
    puzzlePieces = puzzle.split(',')
    puzzlePieces.insert(2, puzzlePieces[1].split('|')[1])
    puzzlePieces[1] = puzzlePieces[1].split('|')[0]

    dividend = make_number(puzzlePieces[2], guess)
    quotient = make_number(puzzlePieces[0], guess)
    divisor = make_number(puzzlePieces[1], guess)
    remainder = make_number(puzzlePieces[len(puzzlePieces) - 1], guess)

    return (dividend, quotient, divisor, remainder)

if __name__ == '__main__':
    main()
