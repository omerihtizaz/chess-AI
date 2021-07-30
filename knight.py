from classes import *

def checkConstraintsInMovements(chess, movements, Family):
    toRemove = set([])
    for movement in movements:
        c, r = movement
        if c < 8 and c > 1:
            if r != 'i' and r != 'j' and r != prev_alpha('a') and r!= prev_alpha(prev_alpha('a')):
                continue
            else:
                toRemove.add(movement)
        else:
            toRemove.add(movement)
    
    for objs in movements:
        if chess.checkEntity:
            if chess.checkCellFamily(objs) == Family:
                toRemove.add(objs)
    for toremove in toRemove:
        movements.remove(toremove)
        
    return movements
def getKnightMovements(board, player):
    movements = []
    coor = player.getCoor()
    movements.append((coor[0] + 1, next_alpha(next_alpha(coor[1]))))
    movements.append((coor[0] - 1, next_alpha(next_alpha(coor[1]))))
    movements.append((coor[0] + 1, prev_alpha(prev_alpha(coor[1]))))
    movements.append((coor[0] - 1, prev_alpha(prev_alpha(coor[1]))))
    movements.append((coor[0] + 2, next_alpha(coor[1])))
    movements.append((coor[0] - 2, next_alpha(coor[1])))
    movements.append((coor[0] + 2, prev_alpha(coor[1])))
    movements.append((coor[0] - 2, prev_alpha(coor[1])))
    return checkConstraintsInMovements(board, movements, player.getFamily())
