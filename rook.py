from classes import *


# rook movements
def horizontalMovementsForRook(chess, player):
    coor = player.getCoor()
    castling = False
    nextAlpha = coor[1]
    movements = []
    while nextAlpha != 'h':
        nextAlpha = next_alpha(nextAlpha)
        if chess.checkEntity((coor[0], nextAlpha)):
            if chess.checkCellFamily((coor[0], nextAlpha)) != player.getFamily():
                movements.append((coor[0], nextAlpha))
                break
            else:
                break
        movements.append((coor[0], nextAlpha))
        if nextAlpha == 'h':
            break
    nextAlpha = coor[1]
    while nextAlpha != 'a':
        nextAlpha = prev_alpha(nextAlpha)
        if chess.checkEntity((coor[0], nextAlpha)):
            if chess.checkCellFamily((coor[0], nextAlpha)) != player.getFamily():
                movements.append((coor[0], nextAlpha))
                break
            else:
                break
        movements.append((coor[0], nextAlpha))
        if nextAlpha == 'a':
            break
    return movements
def verticalMovementsForRook(chess, player):
    coor = player.getCoor()
    movements = []
    current = coor[0]
    while current > 1:
        if chess.checkEntity((current-1, coor[1])):
            if chess.checkCellFamily((current-1, coor[1])) != player.getFamily():
                movements.append((current -1 , coor[1]))
                break
            else:
                break
        movements.append((current -1 , coor[1]))
        current -= 1
    current = coor[0]
    while current < 8:
        if chess.checkEntity((current + 1, coor[1])):
            if chess.checkCellFamily((current + 1 , coor[1])) != player.getFamily():
                movements.append((current + 1 , coor[1]))
                break
            else:
                break
        movements.append((current + 1 , coor[1]))
        current += 1
    return movements

def getRookMovements(board, player):
    return joinList(horizontalMovementsForRook(board, player), verticalMovementsForRook(board, player))
    