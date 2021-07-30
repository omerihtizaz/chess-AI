from bishop import *
from rook import *

def getQueenMovements(board, player):
    return joinList(getBishopMovements(board, player), getRookMovements(board, player))

