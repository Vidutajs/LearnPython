cSet = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '2a': 'wpawn', '2c': 'wpawn'}

#Create new Chessboard 
def createEmptyChessboard():
    chessBoard = []
    for i in range(ord('a'), ord('h')+1, 1) :
        for x in range(8) :
            chessBoard.append(str(x+1) + chr(i))
    return chessBoard

# createChessSet
pieces = {'wpawn': 8, 'wknight': 2, 'wbishop': 2, 'wrook': 2, 'wqueen': 1, 'wking': 1, 'bpawn': 8, 'bknight': 2, 'bbishop': 2, 'brook': 2, 'bqueen': 1, 'bking': 1}

def isValidChessBoard(cBoard) :
    chessBoard = createEmptyChessboard()

    #Check if all board coordinates are legit

    for i in cBoard.keys():
        if i not in chessBoard :
            print('Not a valid Chess Board!')
            return False
    
    #Check if all pieces are legit
    for i in cBoard.values():
        if i not in pieces :
            print('Chess piece is invalid!')
            return False

    #Check piece count
    count = {}
    for piece in cBoard.values() :
        count.setdefault(piece, 0)
        count[piece] = count[piece] + 1
    
    for piece in count.keys():
        if count[piece] > pieces[piece] :
            print('Chess piece count is wrong!')
            return False

    return True    

#just to check
print(isValidChessBoard(cSet))

