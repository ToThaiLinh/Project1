import pygame as p
from position import *
from draw import *
from config import *
import random

def computerMove(screen, board):
    # tìm nước đi của máy
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # return: screen mới cùng board mới
    # -1 : O   ;   1 : X
    position = findBestMove(board)
    print(position)
    drawO(screen, position[1], position[0])
    board[position[0]][position[1]] = -1
    pass

def scores(my_board, next_player, x, y):  
    # phân tích bàn cờ nếu như thêm vào vị trí (x, y)
    # x là hàng, y là cột
    board = coppyList(my_board)
    board[x][y] = next_player
    if have_five(board, next_player, x, y):
        return 1e18
    board[x][y] = -next_player
    if have_five(board, -next_player, x, y):
        return 1e18
    board[x][y] = next_player
    pointAttack = 0
    pointAttack = max(pointAttack, four_in_a_row(board, next_player, x, y, '1'))
    pointAttack = max(pointAttack, three_in_a_row(board, next_player, x, y, '1'))
    pointAttack = max(pointAttack, two_in_a_row(board, next_player, x, y, '1'))
    board[x][y] = -next_player
    pointDefense = 0
    pointDefense = max(pointDefense, four_in_a_row(board, next_player * -1,x , y, '2'))
    pointDefense = max(pointDefense, three_in_a_row(board, next_player * -1, x, y, '2'))
    pointDefense = max(pointDefense, two_in_a_row(board, next_player * -1,x, y, '2'))
    # if( pointAttack > pointDefense ):
    #     return pointAttack
    # else:
    #     return -pointDefense
    return pointAttack + pointDefense

def isValidateRowCol(board, row_index, col_index):
        if 0 <= row_index < len(board) and 0 <= col_index < len(board[0]):
            return True
        return False

def checkLineFromPos(board, playerId, row, col, changeRow, changeCol):
        winningLine = None
        startPoint = None
        endPoint = None
        # Get before squares from pos
        tempRow = row - changeRow
        tempCol = col - changeCol
        count = 1
        startPoint = (row, col)
        while isValidateRowCol(board, tempRow, tempCol) and board[tempRow][tempCol] == playerId:
            count += 1
            startPonit = (tempRow, tempCol)
            tempRow -= changeRow
            tempCol -= changeCol
        
        #Get after squares from pos
        tempRow = row + changeRow
        tempCol = col + changeCol
        while isValidateRowCol(board, tempRow, tempCol) and board[tempRow][tempCol] == playerId:
            count += 1
            endPoint = (tempRow, tempCol)
            tempRow += changeRow
            tempCol += changeCol
        
        # If win, save startPoint and endPoint of winning line
        isWinning = count >= number_score_to_win
        if isWinning:
            winningLine = (startPoint, endPoint)
        return isWinning, count

def getScoreOfPosition(board, playerId, row, col):
        return max(checkLineFromPos(board, playerId, row, col, 1, 0)[1],
                   checkLineFromPos(board, playerId, row, col, 0, 1)[1],
                   checkLineFromPos(board, playerId, row, col, 1, 1)[1],
                   checkLineFromPos(board, playerId, row, col, 1, -1)[1])

def scoreBoard(board):
    if isFull(board):
        return 0
    if isGameOver(board, 1):
        return 1e18
    if isGameOver(board, -1):
        return -1e18
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                score += getScoreOfPosition(board, 1, i, j)
            if board[i][j] == -1:
                score -= getScoreOfPosition(board, -1, i, j)
    return score

def validMoves(board):
    moves = []
    [moves.append((row, col)) for row in range(len(board))
    for col in range(len(board[0])) if board[row][col] == 0]
    return moves

def isGameOver(board, next_player):
    for i in range(len(board)):
        for j in range(len(board[0])):
            return have_five(board, next_player, i, j)

def isFull(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return False
    return True
       
#def scoreBoard(board):
    if isFull(board):
        return 0
    
    if isGameOver(board, 1):
        return 1e18
    
    if isGameOver(board, -1):
        return -1e18
    
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                score += scores(board, 1, i, j)
                score -= scores(board, -1, i, j)
    return score


def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves) - 1)]

def findBestMove(board):
    global nextMove
    nextMove = None
    valid_Moves = validMoves(board)
    random.shuffle(valid_Moves)
    #miniMax(board, valid_Moves, False , dosau)
    MiniMax_AlphaBeta(board, valid_Moves, False, -1e18, 1e18, dosau)
    if nextMove == None:
        nextMove = findRandomMove(valid_Moves)
    return nextMove

def miniMax(board, valid_Moves, isMaxplayer, depth):
    global nextMove
    if depth == 0:
        return scoreBoard(board)
    
    if isGameOver(board, 1 if isMaxplayer else -1):
        return 1e18
    
    if isGameOver(board, -1 if not isMaxplayer else 1):
        return -1e18
    
    if isMaxplayer:
        maxScore = -1e18
        for move in valid_Moves:
            board[move[0]][move[1]] = 1
            nextMoves = []

            #nextMoves = validMoves(board)
            #nextMoves = valid_Moves.remove(move)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        nextMoves.append((i, j))
            
            score = miniMax(board, nextMoves, False, depth - 1)
            if score > maxScore:
                maxScore = score
                if depth == dosau:
                    nextMove = move
            board[move[0]][move[1]] = 0
        return maxScore
    
    if not isMaxplayer:
        minScore = 1e18
        for move in valid_Moves:
            board[move[0]][move[1]] = -1

            nextMoves = []
            #nextMoves = validMoves(board)
            #nextMoves = valid_Moves.remove(move)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        nextMoves.append((i, j))
            
            score = miniMax(board, nextMoves, True, depth - 1)
            if score < minScore:
                minScore = score
                if depth == dosau:
                    nextMove = move
            board[move[0]][move[1]] = 0
        return minScore
'''Hàm miniMax(board, isMax, depth):
            Nếu độ sâu = 0:
                Trả về giá trị của bàn cờ hiện tại
                
            Nếu tất cả các ô đầy:
                Trả về 0
            
            Nếu người chơi chiến thắng (người chơi là max):
                Trả về giá trị lớn nhất
            
            Nếu máy chiến thắng(máy là min):
                Trả về giá trị nhỏ nhất
            
            Nếu là lượt chơi của máy:
                Khởi tạo giá trị min vô cùng lớn 
                Giá trị min = 1e18
                For các ô trống trong bảng:
                    Thực hiện đánh dấu ô trống
                    Tìm các ô trống sau khi đã đi
                    Giá trị trả về = Đệ quy với bảng đã đánh dấu ô trống
                    Nếu giá trị trả về nhỏ hơn giá trị min thì thay thế giá trị min
                Trả về ô trống có giá trị min nhỏ nhất
            
            Nếu là lượt chơi của người chơi:
                Khởi tạo giá trị max vô cùng nhở
                Giá trị max = -1e18
                For các ô trống trong bảng:
                    Thực hiện đánh dấu ô trống
                    Tìm các ô trống sau khi đã đi
                    Giá trị trả về = Đệ quy với bẳng đã đánh dấu ô trống
                    Nếu giá trị trả về lớn hơn giá trị max thì thay thế giá trị max
                Trả về ô trống có giá trị max lớn nhất
    '''
def MiniMax_AlphaBeta(board, valid_Moves, isMaxplayer,alpha, beta, depth):
    global nextMove
    if depth == 0:
        return scoreBoard(board)
    
    if isGameOver(board, 1 if isMaxplayer else -1):
        return 1e18
    
    if isGameOver(board, -1 if not isMaxplayer else 1):
        return -1e18
    
    if isMaxplayer:
        maxScore = -1e18
        for move in valid_Moves:
            board[move[0]][move[1]] = 1
            nextMoves = []
            #nextMoves = validMoves(board)
            #nextMoves = valid_Moves.remove(move)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        nextMoves.append((i, j))
            
            score = miniMax(board, nextMoves, False, depth - 1)
            if score > maxScore:
                maxScore = score
                if depth == dosau:
                    nextMove = move
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            board[move[0]][move[1]] = 0
        return maxScore
    
    if not isMaxplayer:
        minScore = 1e18
        for move in valid_Moves:
            board[move[0]][move[1]] = -1
            nextMoves = []
            #nextMoves = validMoves(board)
            #nextMoves = valid_Moves.remove(move)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        nextMoves.append((i, j))
            
            score = miniMax(board, nextMoves, True, depth - 1)
            if score < minScore:
                minScore = score
                if depth == dosau:
                    nextMove = move
                beta = min(beta, score)
                if beta <= alpha:
                    break
            board[move[0]][move[1]] = 0
        return minScore
    
