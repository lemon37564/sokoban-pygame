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
    
    #258
    #147
    #036
    
                    [2,5,8,1,4,7,0,3,6],#rotate +90degrees from the x axis
    
    #876
    #543
    #210
    
                    [0,1,2,3,4,5,6,7,8][::-1],#[::-1] 顺序相反操作
                    [2,5,8,1,4,7,0,3,6][::-1]]#[3::-1] 从下标为3（从0开始）的元素开始翻转读取
    flipPattern = [[2,1,0,5,4,3,8,7,6],#flipped upside down
    
    #036
    #147
    #258
    
                    [0,3,6,1,4,7,2,5,8],

    #678
    #345
    #012
    
                    [2,1,0,5,4,3,8,7,6][::-1],
                    [0,3,6,1,4,7,2,5,8][::-1]]
    allPattern = rotatePattern + flipPattern

    for box in posBox:
        if box not in posGoals:#box is a 2d tuple (x,y)
            board = [(box[0] - 1, box[1] - 1), (box[0] - 1, box[1]), (box[0] - 1, box[1] + 1), #3*3=9
                    (box[0], box[1] - 1), (box[0], box[1]), (box[0], box[1] + 1), #original pos + 8 moves=9
                    (box[0] + 1, box[1] - 1), (box[0] + 1, box[1]), (box[0] + 1, box[1] + 1)]
            
            for pattern in allPattern:
                newBoard = [board[i] for i in pattern]
                if newBoard[1] in posWalls and newBoard[5] in posWalls: return True
                
                # w
                #w! =>dead
                
                elif newBoard[1] in posBox and newBoard[2] in posWalls and newBoard[5] in posWalls: return True
                
                # ww
                #b! =>dead
                
                elif newBoard[1] in posBox and newBoard[2] in posWalls and newBoard[5] in posBox: return True
                    
                #wb
                #b! =>dead
                
                elif newBoard[1] in posBox and newBoard[2] in posBox and newBoard[5] in posBox: return True
                    
                #bb
                #b! =>dead
                    
                elif newBoard[1] in posBox and newBoard[6] in posBox and newBoard[2] in posWalls and newBoard[3] in posWalls and newBoard[8] in posWalls: return True
                    
                #b b
                #b!  =>dead
                #bb
                  
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
            #print(','.join(node_action[1:]).replace(',',''))
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
        

def generateRandomLevel6X6():#2 goals
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

def generateRandomLevel7X7():#2 goals 
    
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

def generateRandomLevel8X8():#3 goals
    
    character_pos=random.sample(range(36), 17)
  
    map_raw=[' ',' ']
    for i in range(0,34):
        map_raw.append(' ')
    map_raw[character_pos[0]] ='#'
    map_raw[character_pos[1]]='.'
    map_raw[character_pos[2]]='#'
    map_raw[character_pos[3]]='#'
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
    overall_time_start=time.time()
    number_of_goals=-1
    size=-1
    if map_size==6:
        generate_function=generateRandomLevel6X6
        number_of_goals=2
        size=6
    elif  map_size==7:
        generate_function=generateRandomLevel7X7
        number_of_goals=2
        size=7
    elif  map_size==8:
        generate_function=generateRandomLevel8X8
        number_of_goals=3
        size=8
    solvable=False
    method='bfs'
    while not solvable:
        layout = generate_function()
        if(not check_unreachable_goal(layout,number_of_goals,size)):continue
        time_start = time.time()
        #layout, method = readCommand(sys.argv[1:]).values()
        #print(type(layout[0]))
        #print(method)
    
        #print(layout)
        solution=[]
        gameState = transferToGameState(layout)
        posWalls = PosOfWalls(gameState)
        posGoals = PosOfGoals(gameState)
        if method == 'astar':
            result=aStarSearch(gameState,posGoals,posWalls,solution)
        elif method == 'dfs':
            depthFirstSearch(gameState)
        elif method == 'bfs':
            result=breadthFirstSearch(gameState,posGoals,posWalls,solution)
        elif method == 'ucs':
            result=uniformCostSearch(gameState,posGoals,posWalls)
        else:
            raise ValueError('Invalid method.')

        
        #calculate number detours
        char_holder='a'
        detour_len=0
        
        
        for c in solution:
            if((c=='L'or c=='R' or c=='U' or c=='D')and c!=char_holder ):
                detour_len+=1
                char_holder=c
        
        if(result=='solvable'):
            
            if map_size==6:
                if len(solution)>5 and detour_len>3:
                    print("detour_len:"+str(detour_len))
                
                    break
            if map_size==7:
                if len(solution)>5 and detour_len>4:
                    print("detour_len:"+str(detour_len))
                    break
            if map_size==8:
                if len(solution)>5 and detour_len>4:
                    print("detour_len:"+str(detour_len))
                    break
        time_end=time.time()
        #print('Runtime of %s: %.2f second.' %(method, time_end-time_start))
    overall_time_end=time.time()
    print('Overall run time for %dx%d map generation: %.2f seconds.' %(map_size,map_size, overall_time_end-overall_time_start))
    
    return layout

def check_unreachable_goal(s:[],number_of_goals:int,size:int):
    
    for i in range(size):
        for j in range(size):
            if (s[i][j]=='B'):
                    #box surrounded by 4 walls 
                if(
                        s[i][j-1]=='#'
                    and s[i][j+1]=='#'
                    and s[i-1][j]=='#'
                    and s[i+1][j]=='#'
                ):
                    return False
                    #box surrounded by 3 walls
                elif(s[i][j-1]=='#'
                    and s[i][j+1]=='#'
                    and s[i-1][j]=='#'):
                    return False
                elif(s[i][j-1]=='#'
                    and s[i][j+1]=='#'
                    and s[i+1][j]=='#'):
                    return False
                elif( s[i][j-1]=='#'
                    and s[i-1][j]=='#'
                    and s[i+1][j]=='#'):
                    return False
                elif( s[i][j+1]=='#'
                    and s[i-1][j]=='#'
                    and s[i+1][j]=='#'):
                    return False
                    
                    #box in a corner
                elif( s[i][j-1]=='#'
                    and s[i-1][j]=='#'):
                    return False
                    
                elif( s[i-1][j]=='#'
                    and s[i][j+1]=='#'):
                    return False
                    
                elif( s[i][j+1]=='#'
                    and s[i+1][j]=='#'):
                    return False
                    
                elif( s[i+1][j]=='#'
                    and s[i][j-1]=='#'):
                    return False
            elif (s[i][j]=='.'):
                #goal surrounded by 4 walls 
                if(
                    s[i][j-1]=='#'
                    and s[i][j+1]=='#'
                    and s[i-1][j]=='#'
                    and s[i+1][j]=='#'):
                    return False
            elif (s[i][j]==' '):
                    #a space surrounded by walls or boxes
                if(
                        (s[i][j-1]=='#'or s[i][j-1]=='B')
                    and (s[i][j+1]=='#'or s[i][j+1]=='B')
                    and (s[i-1][j]=='#'or s[i-1][j]=='B')
                    and (s[i+1][j]=='#'or s[i+1][j]=='B')):
                        return False

    return True
def evaluate_different_methods(map_size: int):#6 for 6x6,8 for 8x8
    overall_time_start=time.time()
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
    overall_time_end=time.time()
    print('Overall run time for %dx%d map generation: %.2f seconds.' %(map_size,map_size, overall_time_end-overall_time_start))
    
    return layout

if __name__ == '__main__':
    print(generate(8))
    #test map with an unreachable goal
    '''
    s=['######\n',
       '###  #\n',
       '##.# #\n', 
       '###  #\n',
       '#  #&#\n',
       '######']
    print(check_unreachable_goal(s,3,6))'''