# checks if the king is checked or not
def isCheck(chess, family):
    try:
        if returnOtherKing(chess, getOtherColor(family)).getCoor() in  getPossibleMovements(chess, chess.getFamily(getOtherColor(family))):
            return True
        return False
    except:
        return False
# TERMINATING CRITERIA FOR STALEMATE, CHECKMATES
def staleMate(chess, family):
    players = chess.getFamily(family)
    otherplayers = chess.getFamily(getOtherColor(family))
    aMO = []
    for a in otherplayers:
        aMO = joinList(aMO, getMovementsAllowed(chess, a))
    allmovements = []
    for p in players:
        allmovements = joinList(allmovements, getMovementsAllowed(chess, p))
    for aa in allmovements:
        if aa not in aMO:
            return False
    return True
def checkMate2(chess, family):
    king = returnOtherKing(chess, family)
    otherPlayer = chess.getFamily(getOtherColor(family)) 
    players = chess.getFamily(family)
    if len(otherPlayer) == 1:
        allMovements = []
        a = []
        for player in players:
            a = getMovementsAllowed(chess, player)
            allMovements = joinList(allMovements, a)
        movementKing = getMovementsAllowed(chess, king)
        for mK in movementKing:
            if mK not in allMovements:
                return False
        return True
    return False    
def checkMate(chess, family):
    if staleMate(chess, family):
        return "StaleMate"
    king = returnOtherKing(chess, family)
    players = chess.getFamily(family)
    allMovements = []
    a = []
    for player in players:
        a = getMovementsAllowed(chess, player)
        allMovements = joinList(allMovements, a)
    if king.getCoor() in allMovements:
        kingMov = getKingMovements(chess, king)
        for kM in kingMov:
            if kM not in allMovements:
                return False
        return True
    return checkMate2(chess, family)
# CHECKS STALEMATE AND CHECKMATE
def defineChecks(chess, family):
    answer = checkMate(chess, family)
    if answer == "StaleMate":
        return 1
    elif answer:
        return 0
    return -1


def checkCS(chess, family):
    answer = checkMate(chess, family)
    if answer == "StaleMate":
        print("Match Has Ended Due to Stale Mate")
        return True
    elif answer:
        print(family + " Wins")
        return True
    return False
