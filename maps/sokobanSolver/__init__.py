import sys
import collections
import numpy as np
import heapq
import time
import random
class PriorityQueue:
    """Define a PriorityQueue data structure that will be used"""
    def  __init__(self):
        self.Heap = []
        self.Count = 0

    def push(self, item, priority):
        entry = (priority, self.Count, item)
        heapq.heappush(self.Heap, entry)
        self.Count += 1

    def pop(self):
        try:
            (_, _, item) = heapq.heappop(self.Heap)
            
        except :

            return False#empty
        return item

    def isEmpty(self):
        return len(self.Heap) == 0

"""Load puzzles and define the rules of sokoban"""

def transferToGameState(layout):
    #print(type(layout))
    #print(type(layout[1]))
    """Transfer the layout of initial puzzle"""
    layout = [x.replace('\n','') for x in layout]
    layout = [','.join(layout[i]) for i in range(len(layout))]
    layout = [x.split(',') for x in layout]
    maxColsNum = max([len(x) for x in layout])
    for irow in range(len(layout)):
        for icol in range(len(layout[irow])):
            if layout[irow][icol] == ' ': layout[irow][icol] = 0   # free space
            elif layout[irow][icol] == '#': layout[irow][icol] = 1 # wall
            elif layout[irow][icol] == '&': layout[irow][icol] = 2 # player
            elif layout[irow][icol] == 'B': layout[irow][icol] = 3 # box
            elif layout[irow][icol] == '.': layout[irow][icol] = 4 # goal
            elif layout[irow][icol] == 'X': layout[irow][icol] = 5 # box on goal
        colsNum = len(layout[irow])
        if colsNum < maxColsNum:
            layout[irow].extend([1 for _ in range(maxColsNum-colsNum)]) 
    return np.array(layout)

def PosOfPlayer(gameState):
    """Return the position of agent"""
    return tuple(np.argwhere(gameState == 2)[0]) # e.g. (2, 2)

def PosOfBoxes(gameState):
    """Return the positions of boxes"""
    return tuple(tuple(x) for x in np.argwhere((gameState == 3) | (gameState == 5))) # e.g. ((2, 3), (3, 4), (4, 4), (6, 1), (6, 4), (6, 5))

def PosOfWalls(gameState):
    """Return the positions of walls"""
    return tuple(tuple(x) for x in np.argwhere(gameState == 1)) # e.g. like those above

def PosOfGoals(gameState):
    """Return the positions of goals"""
    return tuple(tuple(x) for x in np.argwhere((gameState == 4) | (gameState == 5))) # e.g. like those above

def isEndState(posBox,posGoals):
    """Check if all boxes are on the goals (i.e. pass the game)"""
    return sorted(posBox) == sorted(posGoals)

def isLegalAction(action, posPlayer, posBox,posWalls):
    """Check if the given action is legal"""
    xPlayer, yPlayer = posPlayer
    if action[-1].isupper(): # the move was a push
        x1, y1 = xPlayer + 2 * action[0], yPlayer + 2 * action[1]
    else:
        x1, y1 = xPlayer + action[0], yPlayer + action[1]
    return (x1, y1) not in posBox + posWalls

def legalActions(posPlayer, posBox,posWalls):
    """Return all legal actions for the agent in the current game state"""
    allActions = [[-1,0,'u','U'],[1,0,'d','D'],[0,-1,'l','L'],[0,1,'r','R']]
    xPlayer, yPlayer = posPlayer
    legalActions = []
    for action in allActions:
        x1, y1 = xPlayer + action[0], yPlayer + action[1]
        if (x1, y1) in posBox: # the move was a push
            action.pop(2) # drop the little letter
        else:
            action.pop(3) # drop the upper letter
        if isLegalAction(action, posPlayer, posBox,posWalls):
            legalActions.append(action)
        else: 
            continue     
    return tuple(tuple(x) for x in legalActions) # e.g. ((0, -1, 'l'), (0, 1, 'R'))

def updateState(posPlayer, posBox, action):
    """Return updated game state after an action is taken"""
    xPlayer, yPlayer = posPlayer # the previous position of player
    newPosPlayer = [xPlayer + action[0], yPlayer + action[1]] # the current position of player
    posBox = [list(x) for x in posBox]
    if action[-1].isupper(): # if pushing, update the position of box
        posBox.remove(newPosPlayer)
        posBox.append([xPlayer + 2 * action[0], yPlayer + 2 * action[1]])
    posBox = tuple(tuple(x) for x in posBox)
    newPosPlayer = tuple(newPosPlayer)
    return newPosPlayer, posBox

def isFailed(posBox,posGoals,posWalls):
    """This function used to observe if the state is potentially failed, then prune the search"""
    rotatePattern = [[0,1,2,3,4,5,6,7,8],
                    [2,5,8,1,4,7,0,3,6],
                    [0,1,2,3,4,5,6,7,8][::-1],
                    [2,5,8,1,4,7,0,3,6][::-1]]
    flipPattern = [[2,1,0,5,4,3,8,7,6],
                    [0,3,6,1,4,7,2,5,8],
                    [2,1,0,5,4,3,8,7,6][::-1],
                    [0,3,6,1,4,7,2,5,8][::-1]]
    allPattern = rotatePattern + flipPattern

    for box in posBox:
        if box not in posGoals:
            board = [(box[0] - 1, box[1] - 1), (box[0] - 1, box[1]), (box[0] - 1, box[1] + 1), 
                    (box[0], box[1] - 1), (box[0], box[1]), (box[0], box[1] + 1), 
                    (box[0] + 1, box[1] - 1), (box[0] + 1, box[1]), (box[0] + 1, box[1] + 1)]
            for pattern in allPattern:
                newBoard = [board[i] for i in pattern]
                if newBoard[1] in posWalls and newBoard[5] in posWalls: return True
                elif newBoard[1] in posBox and newBoard[2] in posWalls and newBoard[5] in posWalls: return True
                elif newBoard[1] in posBox and newBoard[2] in posWalls and newBoard[5] in posBox: return True
                elif newBoard[1] in posBox and newBoard[2] in posBox and newBoard[5] in posBox: return True
                elif newBoard[1] in posBox and newBoard[6] in posBox and newBoard[2] in posWalls and newBoard[3] in posWalls and newBoard[8] in posWalls: return True
    return False

"""Implement all approcahes"""

def breadthFirstSearch(gameState,posGoals,posWalls,solution):
    """Implement breadthFirstSearch approach"""
    beginBox = PosOfBoxes(gameState)
    beginPlayer = PosOfPlayer(gameState)

    startState = (beginPlayer, beginBox) # e.g. ((2, 2), ((2, 3), (3, 4), (4, 4), (6, 1), (6, 4), (6, 5)))
    frontier = collections.deque([[startState]]) # store states
    actions = collections.deque([[0]]) # store actions
    exploredSet = set()
    while frontier:
        node = frontier.popleft()
        
        node_action = actions.popleft()
        if(type(node)==bool):
            return "not solvable" 
        if isEndState(node[-1][-1],posGoals):
            print(','.join(node_action[1:]).replace(',',''))
            solution[:]=node_action[1:]
            return "solvable"
            break
        if node[-1] not in exploredSet:
            exploredSet.add(node[-1])
            for action in legalActions(node[-1][0], node[-1][1],posWalls):
                newPosPlayer, newPosBox = updateState(node[-1][0], node[-1][1], action)
                if isFailed(newPosBox,posGoals,posWalls):
                    continue
                frontier.append(node + [(newPosPlayer, newPosBox)])
                actions.append(node_action + [action[-1]])
    return "not solvable" 

def depthFirstSearch(gameState):
    """Implement depthFirstSearch approach"""
    beginBox = PosOfBoxes(gameState)
    beginPlayer = PosOfPlayer(gameState)

    startState = (beginPlayer, beginBox)
    frontier = collections.deque([[startState]])
    exploredSet = set()
    actions = [[0]] 
    while frontier:
        node = frontier.pop()
        node_action = actions.pop()
        if isEndState(node[-1][-1]):
            print(','.join(node_action[1:]).replace(',',''))
            break
        if node[-1] not in exploredSet:
            exploredSet.add(node[-1])
            for action in legalActions(node[-1][0], node[-1][1]):
                newPosPlayer, newPosBox = updateState(node[-1][0], node[-1][1], action)
                if isFailed(newPosBox):
                    continue
                frontier.append(node + [(newPosPlayer, newPosBox)])
                actions.append(node_action + [action[-1]])

def heuristic(posPlayer, posBox,posGoals):
    """A heuristic function to calculate the overall distance between the else boxes and the else goals"""
    distance = 0
    completes = set(posGoals) & set(posBox)
    sortposBox = list(set(posBox).difference(completes))
    sortposGoals = list(set(posGoals).difference(completes))
    for i in range(len(sortposBox)):
        distance += (abs(sortposBox[i][0] - sortposGoals[i][0])) + (abs(sortposBox[i][1] - sortposGoals[i][1]))
    return distance

def cost(actions):
    """A cost function"""
    return len([x for x in actions if x.islower()])

def uniformCostSearch(gameState,posGoals,posWalls):
    """Implement uniformCostSearch approach"""
    beginBox = PosOfBoxes(gameState)
    beginPlayer = PosOfPlayer(gameState)

    startState = (beginPlayer, beginBox)
    frontier = PriorityQueue()
    frontier.push([startState], 0)
    exploredSet = set()
    actions = PriorityQueue()
    actions.push([0], 0)
    while frontier:
        try:
            node = frontier.pop()
            if(type(node)==bool):return "not solvable"
        except:
            return "not solvable"
        node_action = actions.pop()
        if isEndState(node[-1][-1],posGoals):
            print(','.join(node_action[1:]).replace(',',''))
            return "solvable"
            break
        if node[-1] not in exploredSet:
            exploredSet.add(node[-1])
            Cost = cost(node_action[1:])
            for action in legalActions(node[-1][0], node[-1][1],posWalls):
                newPosPlayer, newPosBox = updateState(node[-1][0], node[-1][1], action)
                if isFailed(newPosBox,posGoals,posWalls):
                    continue
                frontier.push(node + [(newPosPlayer, newPosBox)], Cost)
                actions.push(node_action + [action[-1]], Cost)
    

def aStarSearch(gameState,posGoals,posWalls,solution):
    """Implement aStarSearch approach"""
    beginBox = PosOfBoxes(gameState)
    beginPlayer = PosOfPlayer(gameState)

    start_state = (beginPlayer, beginBox)
    frontier = PriorityQueue()
    frontier.push([start_state], heuristic(beginPlayer, beginBox,posGoals))
    exploredSet = set()
    actions = PriorityQueue()
    actions.push([0], heuristic(beginPlayer, start_state[1],posGoals))
    while frontier:
        node = frontier.pop()
        node_action = actions.pop()
        if(type(node)==bool):
            return 'not solvable'
        
        if isEndState(node[-1][-1],posGoals):
            print(','.join(node_action[1:]).replace(',',''))
            solution[:]=node_action[1:]
            return "solvable"
            break
        if node[-1] not in exploredSet:
            exploredSet.add(node[-1])
            Cost = cost(node_action[1:])
            for action in legalActions(node[-1][0], node[-1][1],posWalls):
                newPosPlayer, newPosBox = updateState(node[-1][0], node[-1][1], action)
                if isFailed(newPosBox,posGoals,posWalls):
                    continue
                Heuristic = heuristic(newPosPlayer, newPosBox,posGoals)
                frontier.push(node + [(newPosPlayer, newPosBox)], Heuristic + Cost) 
                actions.push(node_action + [action[-1]], Heuristic + Cost)
    return "not solvable" 
        

def generateRandomLevel6X6():
    character_pos=random.sample(range(16), 13)
    map_raw=[
             ' ',' ',' ',' ',
            ' ', ' ',' ',' ',
            ' ',' ',' ',' ',
            ' ', ' ',' ',' '
            
    ]
    map_raw[character_pos[0]] ='#'
    map_raw[character_pos[1]]='.'
    map_raw[character_pos[2]]='.'
    map_raw[character_pos[3]]='B'
    map_raw[character_pos[4]]='B'
    map_raw[character_pos[5]]='#'
    map_raw[character_pos[6]]='#'
    map_raw[character_pos[7]]='#'
    map_raw[character_pos[8]]='&'
    map_raw[character_pos[9]]='#'
    map_raw[character_pos[10]]=' '
    map_raw[character_pos[11]]=' '
    map_raw[character_pos[12]]='#'

    map_raw_1=["#","#","#","#","#","#"]
    map_raw_1.append("#")
    for i in range(0,4):
        map_raw_1.append(map_raw[i])
    map_raw_1.append("#")
    map_raw_1.append("#")
    for i in range(0,4):
        map_raw_1.append(map_raw[i+4])
    map_raw_1.append("#")
    map_raw_1.append("#")
    for i in range(0,4):
        map_raw_1.append(map_raw[i+8])
    map_raw_1.append("#")
    map_raw_1.append("#")
    for i in range(0,4):
        map_raw_1.append(map_raw[i+12])
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    #WRITE FILE

    s = []
    for i in range(6):
        line = ""
        for j in range(6):
            line += map_raw_1[i*6+j]
        if i < 5:
            line += "\n"
        s.append(line)
    return s

def generateRandomLevel7X7():
    
    character_pos=random.sample(range(25), 15)
  
    map_raw=[' ',' ']
    for i in range(0,23):
        map_raw.append(' ')
    map_raw[character_pos[0]] ='#'
    map_raw[character_pos[1]]='.'
    map_raw[character_pos[2]]='.'
    map_raw[character_pos[3]]='B'
    map_raw[character_pos[4]]='B'
    map_raw[character_pos[5]]=' '
    map_raw[character_pos[6]]=' '
    map_raw[character_pos[7]]='&'
    map_raw[character_pos[8]]='#'
    map_raw[character_pos[9]] ='#'
    map_raw[character_pos[10]]='#'
    map_raw[character_pos[11]] ='#'
    map_raw[character_pos[12]]='#'
    map_raw[character_pos[13]] ='#'
    map_raw[character_pos[14]]='#'

   
    map_raw_1=["#","#","#","#","#","#",'#']
    #ROW 1
    map_raw_1.append("#")
    for i in range(0,5):
        map_raw_1.append(map_raw[i])
    map_raw_1.append("#")
    #ROW 2
    map_raw_1.append("#")
    for i in range(0,5):
        map_raw_1.append(map_raw[i+5])
    map_raw_1.append("#")
    
    #ROW 3
    map_raw_1.append("#")
    for i in range(0,5):
        map_raw_1.append(map_raw[i+10])
    map_raw_1.append("#")

    #ROW 4
    map_raw_1.append("#")
    for i in range(0,5):
        map_raw_1.append(map_raw[i+15])
    map_raw_1.append("#")
    #ROW 5
    map_raw_1.append("#")
    for i in range(0,5):
        map_raw_1.append(map_raw[i+20])
    map_raw_1.append("#")
   

    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    
    #WRTIE
    s = []
    for i in range(7):
        line = ""
        for j in range(7):
            line += map_raw_1[i*7+j]
        if i < 6:
            line += "\n"
        s.append(line)
    return s

def generateRandomLevel8X8():
    
    character_pos=random.sample(range(36), 17)
  
    map_raw=[' ',' ']
    for i in range(0,34):
        map_raw.append(' ')
    map_raw[character_pos[0]] ='#'
    map_raw[character_pos[1]]='.'
    map_raw[character_pos[2]]=' '
    map_raw[character_pos[3]]=' '
    map_raw[character_pos[4]]='B'
    map_raw[character_pos[5]]='#'
    map_raw[character_pos[6]]='#'
    map_raw[character_pos[7]]='#'
    map_raw[character_pos[8]]='#'
    map_raw[character_pos[9]] ='#'
    map_raw[character_pos[10]]='.'
    map_raw[character_pos[12]]='.'
    map_raw[character_pos[13]]='B'
    map_raw[character_pos[14]]='B'
    map_raw[character_pos[15]]='#'
    map_raw[character_pos[16]]='&'
    map_raw_1=["#","#","#","#","#","#",'#','#']
    #ROW 1
    map_raw_1.append("#")
    for i in range(0,6):
        map_raw_1.append(map_raw[i])
    map_raw_1.append("#")
    #ROW 2
    map_raw_1.append("#")
    for i in range(0,6):
        map_raw_1.append(map_raw[i+6])
    map_raw_1.append("#")
    
    #ROW 3
    map_raw_1.append("#")
    for i in range(0,6):
        map_raw_1.append(map_raw[i+12])
    map_raw_1.append("#")

    #ROW 4
    map_raw_1.append("#")
    for i in range(0,6):
        map_raw_1.append(map_raw[i+18])
    map_raw_1.append("#")
    #ROW 5
    map_raw_1.append("#")
    for i in range(0,6):
        map_raw_1.append(map_raw[i+24])
    map_raw_1.append("#")
    #ROW 6
    map_raw_1.append("#")
    for i in range(0,6):
        map_raw_1.append(map_raw[i+30])
    map_raw_1.append("#")

    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    map_raw_1.append("#")
    #WRTIE
    s = []
    for i in range(8):
        line = ""
        for j in range(8):
            line += map_raw_1[i*8+j]
        if i < 7:
            line += "\n"
        s.append(line)
    return s

def generate(map_size: int):#6 for 6x6,8 for 8x8
    if map_size==6:
        generate_function=generateRandomLevel6X6
    elif  map_size==7:
        generate_function=generateRandomLevel7X7
    elif  map_size==8:
        generate_function=generateRandomLevel8X8
    solvable=False
    method='astar'
    while not solvable:
        layout = generate_function()
        time_start = time.time()
        #layout, method = readCommand(sys.argv[1:]).values()
        #print(type(layout[0]))
        #print(method)
    
        print(layout)
        solution=[]
        gameState = transferToGameState(layout)
        posWalls = PosOfWalls(gameState)
        posGoals = PosOfGoals(gameState)
        if method == 'astar':
            result=aStarSearch(gameState,posGoals,posWalls,solution)
        elif method == 'dfs':
            depthFirstSearch(gameState)
        elif method == 'bfs':
            breadthFirstSearch(gameState)
        elif method == 'ucs':
            result=uniformCostSearch(gameState,posGoals,posWalls)
        else:
            raise ValueError('Invalid method.')

        print(result)
        if(result=='solvable'):
            if map_size==6:
                if len(solution)>5:
                    break
            if map_size==7:
                if len(solution)>15:
                    break
            if map_size==8:
                if len(solution)>14:
                    break
        time_end=time.time()
        print('Runtime of %s: %.2f second.' %(method, time_end-time_start))
    return layout


def evaluate_different_methods(map_size: int):#6 for 6x6,8 for 8x8
    if map_size==6:
        generate_function=generateRandomLevel6X6
    elif  map_size==7:
        generate_function=generateRandomLevel7X7
    elif  map_size==8:
        generate_function=generateRandomLevel8X8
    solvable=False
   
    while not solvable:
        layout = generate_function()
        #astar search
        time_start = time.time()
      
    
        print(layout)
        solution=[]
        gameState = transferToGameState(layout)
        posWalls = PosOfWalls(gameState)
        posGoals = PosOfGoals(gameState)
        
        result=aStarSearch(gameState,posGoals,posWalls,solution)
       
        #depthFirstSearch(gameState)
        
        #breadthFirstSearch(gameState)
        
        #result=uniformCostSearch(gameState,posGoals,posWalls)
        

        print(result)
        time_end=time.time()
        print('Runtime of %s: %.2f second.' %('astar', time_end-time_start))

        #bfs
        time_start = time.time()
        solution=[]
        gameState = transferToGameState(layout)
        posWalls = PosOfWalls(gameState)
        posGoals = PosOfGoals(gameState)
        result=breadthFirstSearch(gameState,posGoals,posWalls,solution)
        print(result)
        time_end=time.time()
        print('Runtime of %s: %.2f second.' %('bfs', time_end-time_start))

        if(result=='solvable'):
            if map_size==6:
                if len(solution)>5:
                    break
            if map_size==7:
                if len(solution)>15:
                    break
            if map_size==8:
                if len(solution)>14:
                    break
        
    return layout

if __name__ == '__main__':
    evaluate_different_methods(8)