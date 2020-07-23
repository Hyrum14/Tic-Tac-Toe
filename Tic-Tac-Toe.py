from random import choice
import subprocess as sp

available = []
Xs = set()
Os = set()


def getinput(dimension):
    while True:
        try:
            variable = int(input('Type ' + dimension + ': '))
            break
        except ValueError:
            print('Invalid character')
    return validate(variable)

def choose(player):
    if player:
        Ychoose = 0
        Xchoose = 0
        Ychoose = getinput('row')
        Xchoose = getinput('column')
        while (Ychoose, Xchoose) in Xs:
            Ychoose = getinput('row')
            Xchoose = getinput('column')
        return (Ychoose, Xchoose)
    else:
        return choice(available)


def board():
    for y in '123':
        print(y, end='')
        for x in '123':
            if (int(y), int(x)) in available:
                print('   ', end='')
            elif (int(y), int(x)) in Xs:
                print(' X ', end='')
            else:
                print(' O ', end='')
            if int(x) < 3:
                print('|', end='')
        if int(y) < 3:
            print('\n -----------')
        else:
            print('\n  1   2   3 ')


def diagonal(team):
    ddown = [(1, 1), (2, 2), (3, 3)]
    dup = [(1, 3), (2, 3), (3, 1)]
    if all([square in team for square in ddown]):
        return True
    elif all([square in team for square in dup]):
        return True
    else:
        return False


def won(team):
    for i in '123':
        rowswin = set()
        colswin = set()
        for row, col in team:
            if row == int(i):
                rowswin.add((row, col))
            if col == int(i):
                colswin.add((row, col))
        if len(rowswin) == 3 or len(colswin) == 3 or diagonal(team):
            return True
    return False


def validate(item):
    if item < 1:
        validate(input('Number to small, try again: '))
    if item > 3:
        validate(input('Number to big, try again: '))
    return item


for y in '123':
        for x in '123':
            available.append((int(y), int(x)))
while True:
    sp.call('clear', shell=True)
    board()
    pchoice = choose(True)
    available.remove(pchoice)
    Xs.add(pchoice)
    if won(Xs):
        sp.call('clear', shell=True)
        board()
        print('You won!')
        exit
    cchoice = choose(False)
    available.remove(cchoice)
    Os.add(cchoice)
    if won(Os):
        sp.call('clear', shell=True)
        board()
        print('You lost!')
        exit