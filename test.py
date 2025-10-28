import re
puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"

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

def make_numbers(puzzle, guess):
    puzzlePieces = puzzle.split(',')
    puzzlePieces.insert(2, puzzlePieces[1].split('|')[1])
    puzzlePieces[1] = puzzlePieces[1].split('|')[0]

    dividend = make_number(puzzlePieces[2], guess)
    quotient = make_number(puzzlePieces[0], guess)
    divisor = make_number(puzzlePieces[1], guess)
    remainder = make_number(puzzlePieces[len(puzzlePieces) - 1], guess)

    return (dividend, quotient, divisor, remainder)

print(make_numbers(puzzle, 'TAKEOURSIM'))