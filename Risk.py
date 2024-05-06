import random
class Generation():
    def __init__(self,n):
        self.n = n
    def continents(n):
        board = []
        terNum = (n*(n*3//5))*(80/100)
        conNum = random.randint(4,10)
        conWeight = []
        for i in range(conNum):
            conWeight.append(random.randint(1,n//15))
        tempWeight = 0
        for i in range(len(conWeight)):
            tempWeight += conWeight[i]
        conTerNum = []
        for i in range(conNum):
            conTerNum.append((terNum//tempWeight)*conWeight[i])
        for i in range(len(conTerNum)):
            conTerNum[i]+=random.randint(0,2)
            conTerNum[i]-=random.randint(0,2)
        for r in range(n*3//5):
            tempList = []
            for c in range(n):
                tempList.append(' ')
            board.append(tempList)
        nodeList = []
        blackList = []
        def tListGen():
            tList = [random.randint(1,(n*3//5)-2), random.randint(1,n)-2]
            while tList in blackList:
                tList = [random.randint(1,(n*3//5)-2), random.randint(1,n)-2]
            return tList 
        for i in range(conNum):
            tList = tListGen()
            nodeList.append(tList)
            board[nodeList[i][0]][nodeList[i][1]] = i
            failNum = 0
            count = 0
            cNode = nodeList[i]
            rNode = nodeList[i]
            failMax = n*(n//20)
            while count < conTerNum[i]:
                if failNum > failMax:
                    break
                if count%5 == 0 and rNode != cNode:
                    rNode = cNode
                a = random.randint(int(cNode[0])-1,int(cNode[0])+1)%(n*3//5)
                b = random.randint(int(cNode[1])-1,int(cNode[1])+1)%n
                for m in range(8):
                    if board[a][b] == ' ' and [a,b] not in blackList:
                        cNode = [a,b]
                        board[a][b] = i
                        blackList.append([a,b])
                        count+=1
                if board[a][b] == i:
                    cNode = [a,b]
                    count+=1
                else:
                    failNum+=1
                    cNode = rNode
            for i in range(n*3//5):
                for j in range(n):
                    if board[i][j] != ' ':
                        for r in range(3):
                                for c in range(3):
                                    blackList.append([(i+1-r)%(n*3//5),(j+1-c)%n])
        #>>>
        #Connor, can you add something here that makes it so that every tile bordering the outside of the
        #generated "land" also becomes "land"?(just set all of these newly added "land" points on the board
        #to "%", i'm going to use this later). I put the comment here because the call should only do this
        #one time
        #thanks
        #>>>
        return board
    def forest(n):
        board = Generation.continents(n)
        forestBList = []
        for r in range(n*3//5):
            for c in range(n):
                if board[r][c] != ' ' and [r,c] not in forestBList:
                    target = random.randint(1,n)
                    number = random.randint(1,n)
                    diff = abs(number-target)
                    depoNum = 0
                    if diff < 3:
                        depoNum = number - diff
                    elif diff == 0:
                        depoNum = number
                    rNode = [r,c]
                    cNode = rNode
                    count = 0
                    while count < depoNum:
                        if count%5 == 0 and rNode != cNode:
                            cNode = rNode
                            a = random.randint(int(cNode[0])-1,int(cNode[0])+1)%(n*3//5)
                            b = random.randint(int(cNode[1])-1,int(cNode[1])+1)%n
                            rNode = [a,b]
                            cNode = rNode
                        a = random.randint(int(cNode[0])-1,int(cNode[0])+1)%(n*3//5)
                        b = random.randint(int(cNode[1])-1,int(cNode[1])+1)%n
                        if board[a][b] != ' ' and [a,b] not in forestBList:
                            board[a][b] = '#'
                            cNode = [a,b]
                            forestBList.append(cNode)
                            count+=1
                        elif board[a][b] == '#':
                            cNode = [a,b]
                        else:
                            cNode = rNode
                            count += 1
        return board
    def finalGen(n):
        board = Generation.continents(n)
        board = Generation.forest(n)
        return board
def boardPrint(n):
    board = Generation.continents(n)
    for i in range(n+2):
        print('_',end=' ')
    print()
    for r in range(n*3//5):
        print('|',end=' ')
        for c in range(n):
            print(board[r][c],end=' ')
        print('|')
    for j in range(n+2):
        print('_',end=' ')
def neighbors(grid,type,x,y,n):
    if type == "water":
        # Checks for 1 away
        one_step_checks = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
        for row, col in one_step_checks:
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] != ' ':
                    return 1 
        # check for 2 away
        two_step_checks = [
            (y - 2, x), (y + 2, x), (y, x - 2), (y, x + 2),
            (y - 1, x - 1), (y - 1, x + 1), (y + 1, x - 1), (y + 1, x + 1)
        ]
        for row, col in two_step_checks:
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] != ' ':
                    return 2
        #check for 3 away
        three_step_checks = [
            (y - 3, x), (y + 3, x), (y, x - 3), (y, x + 3),
            (y - 2, x - 1), (y - 2, x + 1), (y + 2, x - 1), (y + 2, x + 1),
            (y - 1, x - 2), (y - 1, x + 2), (y + 1, x - 2), (y + 1, x + 2)
        ]
        for row, col in three_step_checks:
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] != ' ':
                    #adds a 50/50 to make it more random
                    if random.randint(1,2) == 1:
                        return 3
