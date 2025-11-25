import turtle as t

def parta(turnAngle):
    sum = turnAngle
    iterations = 1
    while sum % 360 != 0:
        iterations += 1
        sum += turnAngle
    for i in range(iterations):
        t.left(turnAngle)
        t.forward(300)

def partb(sequence):
    sequenceAngle = 0
    for num in sequence:
        if int(num) == 0:
            sequenceAngle += 30
        else:
            sequenceAngle -= 114
    angle = sequenceAngle
    iterations = 1
    while angle % 360 != 0:
        angle += sequenceAngle
        iterations += 1
    for i in range(iterations):
        for num in sequence:
            if int(num) == 0:
                t.left(30)
                t.forward(40)
            else:
                t.left(-114)
                t.forward(40)

def partc(sequence, zeroAngle, oneAngle):
    for num in sequence:
        if int(num) == 0:
            t.left(zeroAngle)
            t.forward(5)
        else:
            t.left(oneAngle)
            t.forward(5)

def main():
    t.speed(0)
    t.dot(10, "red")
    parta(160)
    input()
    t.reset() # this will clear the turtle window (start over)
    t.speed(0)
    t.dot(10, "red")
    parta(141)
    input()
    t.reset() # this will clear the turtle window (start over)
    t.speed(0)
    t.dot(10, "red")
    partb("01001")
    input()
    t.reset() # this will clear the turtle window (start over)
    t.speed(0)
    t.dot(10, "red")
    partb("01001011")
    input()
    t.reset() # this will clear the turtle window (start over)
    t.speed(0)
    t.dot(10, "red")
    seq1 = "" # create a spiral sequence with 20 ones
    for i in range(20):
        seq1 += "1"
        for j in range(i):
            seq1 += "0"
    partc(seq1, 0, 90)
    input()
    t.reset() # this will clear the turtle window (start over)
    t.speed(0)
    t.dot(10, "red")
    partc(seq1, 0, 30)
    input()
    t.reset() # this will clear the turtle window (start over)
    t.speed(0)
    t.dot(10, "red")
    seq2 = "" # create a spiral sequence with 50 ones
    for i in range(50):
        seq2 += "1"
        for j in range(i):
            seq2 += "0"
    partc(seq2, 0, 150)
    input()
    t.reset() # this will clear the turtle window (start over)
    t.speed(0)
    t.dot(10, "red")
    partc(seq2, 5, 108)
    input()
    t.done() # only need once (at the end) so the window doesn’t close

if __name__ == "__main__":
    main()