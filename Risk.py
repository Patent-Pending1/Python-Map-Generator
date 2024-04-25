import random
def board(n):
    board = []
    terNum = (n**2)*1//5
    if n <= 8:
        conNum = random.randint(3,5)
    elif n > 8 and n < 16:
        conNum = random.randint(5,8)
    else:
        conNum = random.randint(6,10)
    conWeight = []
    for i in range(conNum):
        conWeight.append(random.randint(1,4))
    tempWeight = 0
    for i in range(len(conWeight)):
        tempWeight += conWeight[i]
    conTerNum = []
    for i in range(conNum):
        conTerNum.append((terNum//tempWeight)*conWeight[i])
    if n >= 8:
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
        tList = [random.randint(1,(n*3//5)-2), random.randint(1,n-2)]
        while tList in blackList:
            tList = [random.randint(1,(n*3//5)-2), random.randint(1,n-2)]
        return tList 
    for i in range(conNum):
        tList = tListGen()
        for r in range(n//4):
            for c in range(n//3+1):
                bList = [(tList[0]+(n//4+1)//2-r),(tList[1]+(n//3+1)//2-c)]
                blackList.append(bList)
        nodeList.append(tList)
        board[nodeList[i][0]][nodeList[i][1]] = i
    for i in range(len(nodeList)):
        failNum = 0
        count = 0
        for r in range(int(round(conTerNum[i]**(1/2)))):
            cNode = nodeList[i]
            for c in range(int(round(conTerNum[i]**(1/2)))):
                while count < conTerNum[i]:
                    a = random.randint(int(cNode[0])-1,int(cNode[0])+1)%(n*3//5)
                    b = random.randint(int(cNode[1])-1,int(cNode[1])+1)%n
                    cNode = [a,b]
                    if failNum >= n*2:
                        break
                    if board[a][b] == ' ':
                        board[a][b] = i
                        count+=1
                    else:
                        failNum+=1
                        continue
    for r in range(n*3//5):
        for c in range(n):
            if board[r][c] == 0:
                board[r][c] = '\033[30m#\033[37m'
            elif board[r][c] == 1:
                board[r][c] = '\033[31m#\033[37m'
            elif board[r][c] == 2:
                board[r][c] = '\033[32m#\033[37m'
            elif board[r][c] == 3:
                board[r][c] = '\033[33m#\033[37m'
            elif board[r][c] == 4:
                board[r][c] = '\033[34m#\033[37m'
            elif board[r][c] == 5:
                board[r][c] = '\033[35m#\033[37m'
            elif board[r][c] == 6:
                board[r][c] = '\033[36m#\033[37m'
            elif board[r][c] == 7:
                board[r][c] = '\033[37m#\033[37m'
            elif board[r][c] == 8:
                board[r][c] = '\033[91m#\033[37m'
            elif board[r][c] == 9:
                board[r][c] = '\033[92m#\033[37m'
    return board # i add this to return the board
def boardPrint(n):
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
