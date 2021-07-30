from classes import *


# In[ ]:


# get bishop movements
def getBishopMovements(chess, player):
    coor = player.getCoor()
#     print(coor)
    movement = []
    x = coor[0]
    y = coor[1]
    while (x < 8):
        y = next_alpha(y)
        x = x + 1
        if chess.checkEntity((x, y)):
#             print(chess.getEntity((x, y)).getName(), (x, y))
            if chess.checkCellFamily((x, y)) != player.getFamily():
                movement.append((x, y))
                break
            else:
                break
        else:
            movement.append((x, y))
        
    x = coor[0]
    y = coor[1]
    
    while (x < 8):
        y = prev_alpha(y)
        x = x + 1
        if chess.checkEntity((x , y)):
            if chess.checkCellFamily((x , y)) != player.getFamily():
                movement.append((x, y))
                break
            else:
                break
        else:
            movement.append((x, y))
        
    x = coor[0]
    y = coor[1]
    while (x > 1):
        y = next_alpha(y)
        x = x - 1
        if chess.checkEntity((x, y)):
            if chess.checkCellFamily((x, y)) != player.getFamily():
                movement.append((x, y))
                break
            else:
                break
        else:
            movement.append((x, y))
        
    x = coor[0]
    y = coor[1]
    
    while (x > 1):
        y = prev_alpha(y)
        x = x - 1
        if chess.checkEntity((x, y)):
            if chess.checkCellFamily((x, y)) != player.getFamily():
                movement.append((x, y))
                break
            else:
                break
        else:
            movement.append((x, y))
        
    x = coor[0]
    y = coor[1]
    
    possible = []
    alpha_pos = ['a', 'b', 'c', 'd', 'e', 'f', 'g' , 'h']
    for coor in movement:
        if coor[1] in alpha_pos:
            possible.append(coor)
    return possible
#     


# In[ ]:
