
# checks which player cant move
def inWhich(players, coor):
    for objs in players:
        movements = getMovementsAllowed(objs)
        if len(movements) > 1:
            movements = joinList(movements[0], movements[1])
        if coor in movements:
            return objs
    return False
# returns the next alphabet
def next_alpha(s):
    return chr((ord(s.upper())+1 - 65) % 26 + 65).lower()
# returns the previous alphabet
def prev_alpha(s):
    return chr((ord(s.upper())-1 - 65) % 26 + 65).lower()
# joins 2 lists together
def joinList(A, B):
    result = set([])
    for C in A:
        result.add(C)
    for C in B:
        result.add(C)
    return list(result)
# returns the scores of the players
def getScore(name):
#     Queen: worth 9 points.
# Rook: worth 5 points.
# Bishop: worth 3 points.
# Knight: worth 3 points.
# Pawn: worth 1 point.
# King: worth infinity points, technically.
    if name == 'King':
        return 900000
    elif name == "Queeb":
        return 9
    elif name == 'Rook':
        return 5
    elif name == 'Pawn':
        return 1
    else:# == 'K' and name != 'King':
        return 3
# utility function returning the opposite to the color
def getOtherColor(A):
    if A == 'W':
        return 'B'
    elif A == 'White':
        return "Black"
    elif A == 'Black':
        return 'White'
    return 'W'
# initializes the chess board



# returns the players of that particular color
def getPlayer(board, color, typePlayer):
    players = []
    cells = board.getCells()
    for o in cells:
        player = cells[o].getEntity()
        if player != None:
            if player.getFamily() == color and player.getName() == typePlayer:
                players.append(player)
    return players


# In[8]:


# returns the possible score
def checkOptions(coor):
    playername = chess.getEntityName(coor)
    return getScore(playername)


# In[9]:


def movePlayer(board, newPos,player, real = False):
# moves the player actually in the board, and checks if it just to generate the trees, or to actually  move
    currentPlayerScore = getScore(player.getName())
    finalScore = None
    scorePossible = 0
    currPos = player.getCoor()
    player = board.getCellValue(currPos).getEntity()
    if board.checkEntity(newPos):
        if board.checkCellFamily(newPos) != player.getFamily():
            scorePossible = checkOptions(newPos)
    board.playerDisappear(currPos)
    if board.checkEntity(newPos):
        if real == True:
            p = board.getEntity(newPos)
            if player.getFamily() == "Black":
                print("You have lost a player")
                board.SCORE_COMPUTER += getScore(p.getName())
            else:
                board.SCORE_PLAYER += getScore(p.getName())
                print("You Killed")
            board.playerDisappear(newPos)
        
    board.addPlayer(newPos, player)
    if real == True:
        player.FMD()
    player.setCoor(newPos)
    if scorePossible - currentPlayerScore   ==  (currentPlayerScore) * - 1  :
        return 0
    else:
        return scorePossible - currentPlayerScore


# In[10]:


# returns the king of other color family
def returnOtherKing(chess, family):
    players = chess.getFamily(getOtherColor(family))
    for objs in players:
        if objs.getName() == "King":
            return objs


# In[11]:


# this function returns a random movement 
def returnRandomMovement(Family):
    players = chess.getFamily(Family)
    return getRandomMovements(players)
def isContain(m):
    if m[0].getName() == 'Rook':
        if len(m[1][0]) == 0 and len(m[1][1]) == 0:
            return False
        else:
            movements = []
            for objs in m[1][0]:
                m[1][1].append(objs)
            return m[0],  movements
    if m[0].getName() == 'Queen':
        if len(m[1][0]) == 0 and len(m[1][1][0]) == 0 and len(m[1][1][1]) == 0:
            return False
        else:
            movements = []
            for objs in m[1][1][0]:
                movements.append(objs)
            for objs in m[1][1][1]:
                movements.append(objs)
            return m[0], movements
    elif m[0].getName() == "Pawn":
        if len(m[1][0]) == 0 and len(m[1][1]) == 0:
            return False
        else:
            n = []
            for objs in m[1][0]:
                n.append(objs)
            for objs in m[1][1]:
                n.append(objs)
            return m[0],  n
    else:
        if len(m[1]) == 0:
            return False
        else:
            return m[0],  m[1]
# returns all the possible movements
def getPossibleMovements(chess, players):
    allMovements = []
    for player in players:
        allMovements.append((player, getMovementsAllowed(chess, player)))
    possibleMovements = []
    for objs in allMovements:
        if len(objs[1]) != 0 and type(objs) == type(tuple()):
            possibleMovements.append(objs)
        elif len(objs[1]) != 0 and type(objs) != type(tuple()):
            possibleMovements.append((objs[0], objs[1]))
    return allMovements
# returns the best solution for depth 0
def getBestSolution(chess, Family):
    players = chess.getFamily(Family)
    possibleMovements = getPossibleMovements(chess, players)
    toAdd = []
    for obj in possibleMovements:
        player = obj[0]
        for coor in obj[1]:
            if chess.checkEntity(coor):
                if chess.checkCellFamily(player) != family:
                    name = chess.getEntityName(coor)
                    score = getScore(name)
                    toAdd.append((player, coor, score))
    return toAdd
# returns random movements
def getRandomMovements(chess, players):
    import random
    possibleMovements = getPossibleMovements(chess, players)
    point1 = random.randint(0, len(possibleMovements)-1)
    point2 = random.randint(0, len(possibleMovements[point1]) - 1)
    return possibleMovements[point1][0], possibleMovements[point1][1][point2]
# generates all the possible states from the possible combination of the movements in a given chess board
def generateStates(chess, possibleMov):
    states = []
    n = False
    for objs in possibleMov:
        s = Chess()
        s = s.copy(chess)
        for coor in objs[1]:
            if n == True:
                n = False
                continue
            if type(coor) == type(tuple()):
                score = movePlayer(s, coor , objs[0])
                states.append((s, score, objs[0], coor))
                s = Chess()
                s = s.copy(chess)
            else:
                score = movePlayer(s, (objs[1][0], objs[1][1] ), objs[0])
                states.append((s, score, objs[0], (objs[1][0], objs[1][1] )))
                s = Chess()
                s = s.copy(chess)
                n = True
    return states


# In[12]:


# returns the evaluation of the current chess state
def evaluate(state):
    whiteFam = state[0].getFamily("White")
    blackFam = state[0].getFamily("Black")
    return getScoreForAll(blackFam, state[1], state[0]) - getScoreForAll(whiteFam, state[1], state[0])
###########################################################
# best move for a chess for depth 0, only for testing purpose
def bMove(state):
    bestMove = None
    minEval = float('inf')
    players = state.getFamily("White")
    mov = getPossibleMovements(state, players)
    states = generateStates(state, mov)
    for s in states:
        evala = evaluate(s[0])
        if evala < minEval:
            minEval = evala
    return minEval
def bestMove(state):
    bestMove = None
    maxEval = float('-inf')
    players = state.getFamily("Black")
    mov = getPossibleMovements(state, players )
    states = generateStates(state, mov)
    for s in states:
        evala = evaluate(s[0])
        if evala > maxEval:
            maxEval = evala
            bestMove = s
    return bestMove

#############################################################
# MAIN FUNCTION. 
# RETURNS THE BEST MOVE, MINIMAX VALUE FROM ALL THE POSSIBLE STATES, FOR N DEPTH
def minimax(state, depth,alpha, beta, maximiningAgent):
    if depth == 0:
        evaluateState = evaluate(state)
        return evaluateState , None
    if maximiningAgent:
        bestMove = None
        maxEval = float('-inf')
        players = state[0].getFamily("Black")
        mov = getPossibleMovements(state[0], players)
        states = generateStates(state[0], mov)
        for s in states:
            evala , b = minimax((s[0], s[1]), depth - 1 , alpha, beta, False)
            if evala > maxEval:
                maxEval = evala
                bestMove = (s[2].getCoor(), s[3])
            alpha = max(maxEval, alpha)
            if alpha >= beta:
                break
        return maxEval, bestMove
    else:
        minEval = float('inf')
        bestMove = None
        players = state[0].getFamily("White")
        mov = getPossibleMovements(state[0], players )
        states = generateStates(state[0], mov)
        for s in states:
            evala , b = minimax((s[0], s[1]), depth - 1, alpha, beta, True)
            if evala < minEval:
                minEval = evala
                bestMove = (s[2].getCoor(), s[3])
            alpha = min(minEval, alpha)
            if alpha >= beta:
                break
        return minEval, bestMove