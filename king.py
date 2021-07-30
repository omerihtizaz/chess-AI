from classes import *
# In[ ]:

# returns the movement of the king. checks for the constraints in the very end
def getKingMovements(chess, player):
    movements = []
    coor = player.getCoor()
    if coor[0] > 1:
        movements.append((coor[0] - 1, coor[1]))
        if coor[1] != 'h':
            movements.append((coor[0] - 1, next_alpha(coor[1])))
        if coor[1] != 'a':
            movements.append((coor[0] - 1, prev_alpha(coor[1])))
    if coor[0] < 8:
        movements.append((coor[0] + 1, coor[1]))
        if coor[1] != 'h':
            movements.append((coor[0] + 1, next_alpha(coor[1])))
        if coor[1] != 'a':
            movements.append((coor[0] + 1, prev_alpha(coor[1])))
    if coor[1] != 'h':
        movements.append((coor[0], next_alpha(coor[1])))
    if coor[1] != 'a':
        movements.append((coor[0], prev_alpha(coor[1])))
    toRemove = []
    for coor in movements:
        if chess.checkEntity(coor):
            if chess.checkCellFamily(coor) == player.getFamily():
                toRemove.append(coor)
    for objs in toRemove:
        movements.remove(objs)
    return movements


# In[ ]:
