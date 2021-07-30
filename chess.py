#!/usr/bin/env python
# coding: utf-8
from game import *
# In[1]:




# In[ ]:


def getMovementsAllowed(board, player):
    if player.getName()[0] == "P":
        return getPawnMovements(board, player)
    if player.getName()[0] == 'B':
        return getBishopMovements(board, player)
    if player.getName()[0] == 'R':
        return getRookMovements(board, player)
    if player.getName()[0] == 'Q':
        return getQueenMovements(board, player)
    if player.getName() == 'King':
        return getKingMovements(board, player)
    if player.getName()[0] == 'K' and player.getName() != 'King':
        return getKnightMovements(board, player)
    


# In[4]:




def initialize():
    chessBoard = Chess()
    yaxis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    initial = 'B'
    for i in reversed(range(1, 9)):
        for j in yaxis:
            if i == 7:
                p = player(i, j, "Pawn", "Black")
            elif i == 2:
                p = player(i, j, "Pawn", "White")
            else:
                p = None
            initial = getOtherColor(initial)
            chessBoard.setCell(i, j,initial, p)
        initial = getOtherColor(initial)
    chessBoard.addPlayer((1,'e'), player(1,'d','Queen', 'White'))
    chessBoard.addPlayer((8,'e'), player(8,'d','Queen', 'Black'))
    chessBoard.addPlayer((1,'d'), player(1,'e', 'King', 'White'))
    chessBoard.addPlayer((8,'d'), player(8,'e', 'King', 'Black'))
    chessBoard.addPlayer((1,'c'), player(1,'c','Bishop', 'White'))
    chessBoard.addPlayer((8,'c'), player(8,'c','Bishop', 'Black'))
    chessBoard.addPlayer((1,'f'), player(1,'f', 'Bishop', 'White'))
    chessBoard.addPlayer((8,'f'), player(8,'f','Bishop', 'Black'))
    chessBoard.addPlayer((1,'b'), player(1,'b','Knight', 'White'))
    chessBoard.addPlayer((8,'b'), player(8,'b', 'Knight', 'Black'))
    chessBoard.addPlayer((1,'g'), player(1,'g','Knight', 'White'))
    chessBoard.addPlayer((8,'g'), player(8,'g', 'Knight', 'Black'))
    chessBoard.addPlayer((1,'a'), player(1,'a','Rook', 'White'))
    chessBoard.addPlayer((8,'a'), player(8,'a','Rook', 'Black'))
    chessBoard.addPlayer((1,'h'), player(1,'h','Rook', 'White'))
    chessBoard.addPlayer((8,'h'), player(8,'h', 'Rook', 'Black'))
#     chessBoard.printChess()     
    return chessBoard   
# In[5]:


# returns the score for all the players. 
# this function is used in evaluation criteria
# in simple demostration, only the number of players from the black are substracted from
# the number of players from the white, however there are certain moves which are favoured over other moves
# for example, killing of a knight/queen/bishop/rook from a pawn is much much more profitable than killing
# it from your queen and ending up dead
def getScoreForAll(players, deCaprio, state):
    score = 0.0
    middle = [4, 5]
    average = [3, 6]
    b = [1, 2, 3]
    w = [5, 6, 7]
# hence some moves are given bonus points, for example pawn movements are more favoured in the start, 
# knight movements in the middle are more favoured. 
    if isCheck(state, players[0].getFamily()):
        score += 7
    DC = defineChecks(chess, players[0].getFamily())
    if DC == 1 or DC == 0:
        score += 15
    for player in players:
        if deCaprio == 0 and player.getName() == "Pawn" and not player.getFM():
            score += 0.2
        elif deCaprio == 0 and player.getName() == "Pawn" and player.getFM():
            score += 0.1
        elif deCaprio > 0.5 and player.getName() == "Pawn":
            score += 0.3
        elif deCaprio > 2 and player.getName() == "Pawn":
            score += 2
        x = player.getCoor()[0]
        y = player.getCoor()[1]
        if player.getName() == "Knight":
            if x in middle:
                score += 0.3
            elif (player.getFamily() == 'Black' and x in b)  or  (player.getFamily() == "White" and x in w):
                score += 0.2
            elif (player.getFamily() == 'Black' and x in w)  or  (player.getFamily() == "White" and x in b):
                score += 0.1
            else:
                score += 0.05
# similarly rook should not be cornered. hence a small bonus if not cornered
        if player.getName() == 'Rook':
            if player.getFamily() == 'White' and x == 1:
                if y == 'a' or y == 'h':
                    score -= 0.1
            elif player.getFamily() == 'Black' and x == 8:
                if y == 'a' or y == 'h':
                    score -= 0.1            
        score += getScore(player.getName())
    return score


# In[6]:


chess = Chess()


# In[7]:

# CALLS THE MINIMAX AND MOVES THE COMPUTER AS PER RESULT
def getNext(chess, depth):
    alpha = minimax((chess, 0), depth, float('-inf') , float('inf') , True )
    curr = alpha[1][0]
    nex = alpha[1][1]
    en = chess.getEntity(curr)
    print(en.getName() + " moved from ", end = '')
    print(curr, " to ", nex)
    movePlayer(chess, nex, en , True)
#     chess.printChess()


# In[13]:


# UI FOR PLAYER
def MovePlayer():
    while True:
        name = input("Enter Key's current_pos: ")
        try:
            entity = chess.getEntity((int(name.split(' ')[0]) , name.split(' ')[1]))
            print(entity.getName())
            print("Possible Movements: ")
            movements = getMovementsAllowed(chess, entity)
            for m in movements:
                print(m, end = ' -|- ')
            print()
        except:
            print("Wrong cell: ")
            print("Enter Again!: ")
            name = input("Enter Key's current_pos: ")
            entity = chess.getEntity((int(name.split(' ')[0]) , name.split(' ')[1]))
            print(entity.getName())
            print("Possible Movements: ")
            movements = getMovementsAllowed(chess, entity)
            for m in movements:
                print(m, end = ' -|- ')
            print()
        choice = input("Would you like to choose another?[Y/N]: ")
        while choice == 'Y' or choice == 'N':
            name = input("Enter Key's current_pos: ")
            entity = chess.getEntity((int(name.split(' ')[0]) , name.split(' ')[1]))
            print(entity.getName())
            print("Possible Movements: ")
            movements = getMovementsAllowed(chess, entity)
            print(' -|- ', end = '')
            for m in movements:
                print(m, end = ' -|- ')
            print()
            choice = input("Would you like to choose another?[Y/N]: ")
        coor = input("Enter New Position: ")
        a = int(coor.split(' ')[0])
        b = coor.split(' ')[1]
        if (a, b) in movements:
            movePlayer(chess, (a, b), entity, True)
            break
        else:
            print("Cant Move there! ")
def MoveComputer():
    getNext(chess, 3)


# In[14]:


# In[15]:


# MAIN
def main(a = False):
    while True:
        if not a:
            chess.printChess()
            a = True
        print("\n-----------------------------------------------------------------------------------------")
        print()
        MovePlayer()
        if checkCS(chess, 'White'):
            return
        print("Waiting for AI Turn")
        MoveComputer()
        if checkCS(chess, 'Black'):
            return
        chess.printChess()
        print("\n-----------------------------------------------------------------------------------------")
        
        


# In[18]:


chess = initialize()


# In[ ]:


main()


# In[ ]:




