import random
def Board(n):
    board = []
    terNum = (n**(3/2))
    #^^^Temporary placeholder values, must change later
    conNum = random.randint(6,15)
    #^^^"
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
            if count > 5:
                a = random.randint(int(cNode[0])-1,int(cNode[0])+1)%(n*3//5)
                b = random.randint(int(cNode[1])-1,int(cNode[1])+1)%n
                neighborList = []
                for r in range(3):
                    for c in range(3):
                        neighborList.append(board[(cNode[0]+1-r)%(n*3//5)][(cNode[1]+1-r)%n])
                if neighborList.count(i) <= 2:
                    continue
            else:
                a = random.randint(int(cNode[0])-1,int(cNode[0])+1)%(n*3//5)
                b = random.randint(int(cNode[1])-1,int(cNode[1])+1)%n
            if board[a][b] == ' ' and [a,b] not in blackList:
                cNode = [a,b]
                board[a][b] = i
                blackList.append([a,b])
                count+=1
            elif board[a][b] == i:
                cNode = [a,b]
            else:
                failNum+=1
                cNode = rNode
        for i in range(n*3//5):
            for j in range(n):
                if board[i][j] != ' ':
                    for r in range(3):
                            for c in range(3):
                                blackList.append([(i+1-r)%(n*3//5),(j+1-c)%n])
    return board
def boardPrint(n):
    board = Board(n)
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
