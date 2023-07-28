#dictionary for the board
board = dict(a8 ="[   B Rook   ]", b8 ="[  B Horse   ]", c8 ="[  B Bishop  ]", d8 ="[  B Queen   ]", e8 ="[   B King   ]", f8 ="[  B Bishop  ]", g8 ="[  B Horse   ]", h8 ="[   B Rook   ]",
            a7 ="[   B Pawn   ]", b7 ="[   B Pawn   ]", c7 ="[   B Pawn   ]", d7 ="[   B Pawn   ]", e7 ="[   B Pawn   ]", f7 ="[   B Pawn   ]", g7 ="[   B Pawn   ]", h7 ="[   B Pawn   ]",
            a6 ="[            ]", b6 ="[            ]", c6 ="[            ]", d6 ="[            ]", e6 ="[            ]", f6 ="[            ]", g6 ="[            ]", h6 ="[            ]",
            a5 ="[            ]", b5 ="[            ]", c5 ="[            ]", d5 ="[            ]", e5 ="[            ]", f5 ="[            ]", g5 ="[            ]", h5 ="[            ]",
            a4 ="[            ]", b4 ="[            ]", c4 ="[            ]", d4 ="[            ]", e4 ="[            ]", f4 ="[            ]", g4 ="[            ]", h4 ="[            ]",
            a3 ="[            ]", b3 ="[            ]", c3 ="[            ]", d3 ="[            ]", e3 ="[            ]", f3 ="[            ]", g3 ="[            ]", h3 ="[            ]",
            a2 ="[   W Pawn   ]", b2 ="[   W Pawn   ]", c2 ="[   W Pawn   ]", d2 ="[   W Pawn   ]", e2 ="[   W Pawn   ]", f2 ="[   W Pawn   ]", g2 ="[   W Pawn   ]", h2 ="[   W Pawn   ]",
            a1 ="[   W Rook   ]", b1 ="[  W Horse   ]", c1 ="[  W Bishop  ]", d1 ="[  W Queen   ]", e1 ="[   W King   ]", f1 ="[  W Bishop  ]", g1 ="[  W Horse   ]", h1 ="[   W Rook   ]",)

#a loop where if the king is still in the dictionary then the game continues
while ("[   B King   ]" in board.values()) and ("[   W King   ]" in board.values()):

    #print each row of the board with the rows number before it and the row above it
    print() #distance
    print("Row               a             b             c             d             e             f             g             h")
    print(("8           ") + board['a8'] + board['b8'] + board['c8'] + board['d8'] + board['e8'] + board['f8'] + board['g8'] + board['h8'])
    print(("7           ") + board['a7'] + board['b7'] + board['c7'] + board['d7'] + board['e7'] + board['f7'] + board['g7'] + board['h7'])
    print(("6           ") + board['a6'] + board['b6'] + board['c6'] + board['d6'] + board['e6'] + board['f6'] + board['g6'] + board['h6'])
    print(("5           ") + board['a5'] + board['b5'] + board['c5'] + board['d5'] + board['e5'] + board['f5'] + board['g5'] + board['h5'])
    print(("4           ") + board['a4'] + board['b4'] + board['c4'] + board['d4'] + board['e4'] + board['f4'] + board['g4'] + board['h4'])
    print(("3           ") + board['a3'] + board['b3'] + board['c3'] + board['d3'] + board['e3'] + board['f3'] + board['g3'] + board['h3'])
    print(("2           ") + board['a2'] + board['b2'] + board['c2'] + board['d2'] + board['e2'] + board['f2'] + board['g2'] + board['h2'])
    print(("1           ") + board['a1'] + board['b1'] + board['c1'] + board['d1'] + board['e1'] + board['f1'] + board['g1'] + board['h1'])

    #asks for the cordinate of the piece you want to move, the dictionaries key
    ocord = input("what piece would you like to move? ")

    #uses the dictionarys key to give the value to follow with the print
    selectedpiece = board[ocord]
    print("Selected: " + selectedpiece)

    #asks for the cordinate of where your moving to
    ncord = input("Where do you want to move the piece? ")

    #replaces the new cordinate's value with the moved piece's value
    board[ncord] = selectedpiece

    #replaces the old cordinate with a blank spot
    board[ocord] = '[            ]'
else:
    print()  # distance
    print("Row               a             b             c             d             e             f             g             h")
    print(("8           ") + board['a8'] + board['b8'] + board['c8'] + board['d8'] + board['e8'] + board['f8'] + board[
        'g8'] + board['h8'])
    print(("7           ") + board['a7'] + board['b7'] + board['c7'] + board['d7'] + board['e7'] + board['f7'] + board[
        'g7'] + board['h7'])
    print(("6           ") + board['a6'] + board['b6'] + board['c6'] + board['d6'] + board['e6'] + board['f6'] + board[
        'g6'] + board['h6'])
    print(("5           ") + board['a5'] + board['b5'] + board['c5'] + board['d5'] + board['e5'] + board['f5'] + board[
        'g5'] + board['h5'])
    print(("4           ") + board['a4'] + board['b4'] + board['c4'] + board['d4'] + board['e4'] + board['f4'] + board[
        'g4'] + board['h4'])
    print(("3           ") + board['a3'] + board['b3'] + board['c3'] + board['d3'] + board['e3'] + board['f3'] + board[
        'g3'] + board['h3'])
    print(("2           ") + board['a2'] + board['b2'] + board['c2'] + board['d2'] + board['e2'] + board['f2'] + board[
        'g2'] + board['h2'])
    print(("1           ") + board['a1'] + board['b1'] + board['c1'] + board['d1'] + board['e1'] + board['f1'] + board[
        'g1'] + board['h1'])


    print("GAME OVER!    GREAT GAME!")