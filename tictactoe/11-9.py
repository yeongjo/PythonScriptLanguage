matrix = [] #전역변수 : 6x6 틱택토 보드 자료구조

def drawBoard():
    for i in range(6):
        print('----------------------')
        for j in range(6):
            print('|',matrix[i][j],' ',end='')
        print('|')
    print('----------------------')

def check():    #4개 연속인 것을 찾으면 o or x 를 찾아서 반환 아니면 빈문자 반환
    # 가로 4개 체크
    for i in range(6):  #행과 열 가로/세로에 대해서 3개 연속 검사
        for j in range(3): #col =0,1,2,3
            player = matrix[i][j]   #i행의 4개 열이 연속인지 검사 (가로)
            if player != ' ' and player == matrix[i][j+1] and player == matrix[i][j+2] and player == matrix[i][j+3]:
                return player

    for i in range(3):  #행과 열 가로/세로에 대해서 3개 연속 검사
        for j in range(6): #col =0,1,2,3
            player = matrix[i][j]   #i행의 4개 열이 연속인지 검사 (가로)
            if player != ' ' and player == matrix[i+1][j] and player == matrix[i+2][j] and player == matrix[i+3][j]:
                return player

    # 대각선 검사
    for i in range(3):
        for j in range(4):
            player = matrix[i][j]   # 왼 위 오른 아래
            if player != ' ' and player == matrix[i+1][j+1] and player == matrix[i+2][j+2] and player == matrix[i+3][j+3]:
                return player

    for i in range(3):
        for j in range(4):
            player = matrix[i][j]   # 왼 위 오른 아래
            if player != ' ' and player == matrix[i+1][j-1] and player == matrix[i+2][j-2] and player == matrix[i+3][j-3]:
                return player
    return ''

def findRow(col):
    for row in range(5,-1,-1): #row=5,4,3,2,1,0
        if matrix[row][col] == ' ':
            return row
    return 6

def main():
    for i in range(6):
        matrix.append([])
        for j in range(6):
            matrix[i].append(' ')   #공란 문자열 삽입

    drawBoard()
    turn = True
    while True:
        col = -1
        if turn:
            col = eval(input('열 0-6에 빨간색 디스크를 떨어트리세요 입력: '))
        else:
            col = eval(input('열 0-6에 노란색 디스크를 떨어트리세요 입력: '))


        row = findRow(col)
        while row != 6:
            if turn:
                matrix[row][col] = 'R'
            else:
                matrix[row][col] = 'Y'
            break
        else:
            print("꽉찬 열입니다. 다시 떨어트리세요")

        drawBoard()
        player = check()
        if player != '':
            if player == 'R':
                print('빨간색 플레이어가 이겼습니다.')
            else:
                print('노란색 플레이어가 이겼습니다.')
            break
        turn = not turn

main()