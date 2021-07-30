from classes import *
# these are the functions required for the pawn get possible movements
# returns a list of tuples
def returnUp(chess, player):
    coor = player.getCoor()
    fam = player.getFamily()
    movements = []
    if fam == 'White':
        movements.append((coor[0] + 1, coor[1]))
        if not player.getFM():
            movements.append((coor[0] + 2, coor[1]))
    else:
        movements.append((coor[0] - 1, coor[1]))
        if not player.getFM():
            movements.append((coor[0] - 2, coor[1]))
    toremove = []
    for objs in movements:
        if objs[0] > 8 or objs[0] < 1 or chess.checkEntity(objs):
            toremove.append(objs)
    for objs in toremove:
        movements.remove(objs)
        
    return movements

# diagonal movement for pawn
def getDiagonalMovement(chess, player):
        coor = player.getCoor()
        family = player.getFamily()
        possible = []
        if family == "Black":
            if coor[1] != 'h':
                if coor[0] > 1:
                    if chess.checkEntity((coor[0]-1 ,next_alpha(coor[1]))):
                        if chess.checkCellFamily((coor[0]-1 ,next_alpha(coor[1]))) != player.getFamily():
                            possible.append((coor[0]-1 ,next_alpha(coor[1])))
                            
            if coor[1] != 'a':
                if coor[0] > 1:
                    if chess.checkEntity((coor[0]-1 ,prev_alpha(coor[1]))):
                        if chess.checkCellFamily((coor[0]-1 ,prev_alpha(coor[1]))) != player.getFamily():
                            possible.append((coor[0]-1 ,prev_alpha(coor[1])))
        else:
            if coor[1] != 'h':
                if coor[0] < 8:
                    if chess.checkEntity((coor[0]+1 ,next_alpha(coor[1]))):
                        if chess.checkCellFamily((coor[0]+1 ,next_alpha(coor[1]))) != player.getFamily():
                            possible.append((coor[0]+1 ,next_alpha(coor[1])))
            if coor[1] != 'a':
                if coor[0] < 8:
                    if chess.checkEntity((coor[0]+1 ,prev_alpha(coor[1]))):
                        if chess.checkCellFamily((coor[0]+1 ,prev_alpha(coor[1]))) != player.getFamily():
                            possible.append((coor[0]+1 ,prev_alpha(coor[1])))
        return possible
def getPawnMovements(board, player):
    return joinList(returnUp(board, player), getDiagonalMovement(board, player))


# In[ ]: