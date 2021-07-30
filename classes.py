
# In[2]:

from functions import *
# player or key class
class player:
    def __init__(self, x , y, name, family):
        self.name = name
        self.family = family
        self.x = x
        self.y = y
        self.firstMovement = False
    def copy(self, A):
        self.name = A.name
        self.family = A.family
        self.x = A.x
        self.y = A.y
        self.firstMovement = A.firstMovement
#     used to detect the first movement of the pawn
    def FMD(self):
        self.firstMovement = True
    def getFM(self):
        return self.firstMovement
    def getX(self):
        return self.x
    def getY(self):
        return self.Y
    def getCoor(self):
        return self.x, self.y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setCoor(self, coor):
        self.x = coor[0]
        self.y = coor[1]
    def getName(self):
        return self.name
    def getFamily(self):
        return self.family
# class for a particular chess cell and it's attributes
class chessCell:
    def __init__ (self, x, y, color, entity = None, isEmpty = True):
        self.color = color
        self.x = x
        self.y = y
        self.entity = entity
        if entity !=  None:
            self.isEmpty = False
        else:
            self.isEmpty = isEmpty
    def copy (self, A):
        self.color = A.color
        self.x = A.x
        self.y = A.y
        self.entity = A.entity
        if entity !=  None:
            self.isEmpty = False
        else:
            self.isEmpty = isEmpty
    def getColor(self):
        return self.color
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getCoordinates(self):
        return self.x, self.y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def getEntity(self):
        return self.entity
    def setCoor(self, coor):
        self.x = coor[0]
        self.y = coor[1]
    def setColor(self, color):
        self.color = color
    def setEntity(self, entity):
        self.entity = entity
        self.isEmpty = False
    def removeEntity(self):
        self.entity = None
        self.isEmpty = True
    def isItEmpty(self):
        return self.isEmpty
    def printCell(self):
        try:
            if self.entity.getFamily() == 'Black':
                if self.entity.name == 'Pawn' or self.entity.name == 'King'or self.entity.name == 'Rook':
                    print(""" '"""+self.entity.name+ """' """, end = '   ')
                elif self.entity.name == 'Queen':
                    print(""" '"""+self.entity.name+ """'""", end = '   ')
                else:
                    print("""'"""+self.entity.name+ """'""", end = '   ')
            else:
                if self.entity.name == 'Pawn' or self.entity.name == 'King'or self.entity.name == 'Rook':
                    print("  " + self.entity.name + "  ", end = '   ')
                elif self.entity.name == "Knight" or self.entity.name == 'Bishop':
                    print( " " + self.entity.name + " ", end = '   ')
                else:
                    print( "  " + self.entity.name + " ", end = '   ')
                    
        except:
            print("    " + self.color + "   ", end = '   ')
# class of a combination of all chess cells
class Chess:
    def __init__ (self):
        self.maxWidth = 8
        self.maxHeight = 8
        self.cells = {}
        self.SCORE_PLAYER = 0
        self.SCORE_COMPUTER = 0
    def copy(self, A):
        self.maxWidth = A.maxWidth
        self.maxHeight = A.maxHeight
        self.SCORE_PLAYER, self.SCORE_COMPUTER = A.getScores()
        self.cells = {}
        for objs in A.cells:
            currentChessCell = A.cells[objs]
            currentChessEntity = currentChessCell.getEntity()
            if currentChessEntity != None:
                x = currentChessCell.getX()
                y = currentChessCell.getY()
                c = currentChessCell.getColor()
                name = currentChessEntity.getName()
                family = currentChessEntity.getFamily()
                fm = currentChessEntity.getFM()
                p = player(x, y, name, family)
                empty = currentChessCell.isItEmpty
                if fm == True:
                    p.FMD()
                self.cells[objs] = chessCell(x, y, c , p, empty)
            else:
                x = currentChessCell.getX()
                y = currentChessCell.getY()
                c = currentChessCell.getColor()
                self.cells[objs] = chessCell(x, y, c , None, True)
        return self
    def generateState(self):
        return self
    def getScores(self):
        return self.SCORE_PLAYER, self.SCORE_COMPUTER
    def setCell(self, x,y,color, entity = None, isEmpty = True):
        self.cells[(x, y)] = chessCell(x,y,color, entity, isEmpty)
    def addPlayer(self, coor, entity):
        self.cells[coor].setEntity(entity)
    def getEntity(self, coor):
        try:
            return self.cells[coor].getEntity()
        except:
            return False
    def checkCellFamily(self, coor):
        try:
            return self.cells[coor].getEntity().getFamily()
        except:
            return False
    def printChess(self):
        global SCORE_PLAYER
        global SCORE_COMPUTER
        a = prev_alpha('a')
        print("\t", end = '')
        for i in range(0, 8):
            if i == 8:
                print("    " + next_alpha(a) + "   ")
                break
            print("    " + next_alpha(a) + "   ", end = '   ')
            a = next_alpha(a)
        current = 0
        curr = 9
        
        for objs in self.cells:
            if current % 8 == 0:
                print("    ", curr, "   ")
                curr -= 1
                current = 0
                print('\n')
            if current == 0:
                print("    ", curr, "   ", end = '')
            self.cells[objs].printCell()
            
            current += 1
        print('')
        print('')
        print('\t', end = '')
        a = prev_alpha('a')
        for i in range(0, 8):
            print("    " + next_alpha(a) + "   ", end = '   ')
            a = next_alpha(a)
        print('')
        print("White: ", self.SCORE_PLAYER)
        print("Black: ", self.SCORE_COMPUTER)
    def checkEntity(self, coor):
        try:
            if self.cells[coor].getEntity() != None:
                return True
        except:
            return False
    def getFamily(self, Family):
        players = []
        for coor in self.cells:
            try:
                if self.cells[coor].getEntity().getFamily() == Family:
                    players.append(self.cells[coor].getEntity())
            except:
                continue
        return players
    def getCells(self):
        return self.cells
    def isTherePlayer(self, coor):
        return not self.cells[coor].isItEmpty()
    def playerDisappear(self, coor):
        self.cells[coor].removeEntity()
    def getPlayer(self, name , fam):
        players = []
        for coor in self.cells:
            
            try:
                if self.cells[coor].getEntity().getFamily() == fam and self.cells[coor].getEntity().getName() == name:
                    players.append(self.cells[coor].getEntity())
            except:
                continue
        return players
                
    def getCellValue(self, coor):
        return self.cells[coor]
    def getEntityName(self, coor):
        try:
            return self.cells[coor].getEntity().getName()
        except:
            return False
        



# In[3]: