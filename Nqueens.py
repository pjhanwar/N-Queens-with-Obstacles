import sys
import queue
import random
import math
import datetime

def getBoard():
    fname = "input.txt"
    output_file = "output.txt"
    global board_size
    global no_of_lizards
    try:
        input_file = open(fname, 'r')
        lines = input_file.readlines()
        for index, line in enumerate(lines):
            if index == 1:
                board_size = int(lines[index].strip("\n"))
                no_of_lizards = int(lines[index + 1].strip("\n"))
                board = []
                for i in range(2, board_size + 2):
                    board.append(list(lines[index + i].strip("\n")))
                if ("DFS" in lines[index - 1]) or (("Depth First Search").casefold() in lines[index - 1]):
                    if DFS(0, 0, 0, board):
                        break
                    else:
                        #print("FAIL\n")
                        fo = open(output_file, 'w')
                        fo.write("FAIL\n")
                        fo.close()
                elif ("BFS" in lines[index - 1]) or (("Breadth First Search").casefold() in lines[index - 1]):
                    if not(BFS(board)):
                        fo = open(output_file, 'w')
                        fo.write("FAIL\n")
                        fo.close()
                    break
                elif ("SA" in lines[index - 1]) or (("Simulated Annealing").casefold() in lines[index - 1]):
                    if SA(board_size, no_of_lizards, board):
                        break
                    else:
                        #print("FAIL\n")
                        fo = open(output_file, 'w')
                        fo.write("FAIL\n")
                        fo.close()
                    break
                else:
                    fo = open(output_file, 'w')
                    fo.write("FAIL\nPlease Enter proper search algorithm")
                    input_file.close()
                    fo.close()
                    sys.exit()
        input_file.close()
    except IOError:
        fo = open(output_file, 'w')
        fo.write("FAIL\nFile not found: {}".format(fname))
        fo.close()
        sys.exit()

#------------------------------------------------------------------------#
#------------------------------------------------------------------------#

def DFS(row, column, liz_cnt, board):
    #print("\nIN DFS\n")
    global board_size
    global no_of_lizards
    n = board_size
    l = no_of_lizards
    cnt = liz_cnt
    board_copy = [k[:] for k in board]
    flg = 0
    for i in range(column,n):
        cnt = liz_cnt
        board_copy = [k[:] for k in board]
        if safe_to_place(board_copy,row,i):
            flg=1
            board_copy[row][i] = '1'
            cnt += 1

            if cnt == l:
                fo = open("output.txt", 'w')
                fo.write("OK\n")
                for a in board_copy:
                    fo.write("".join(map(str, a)) + "\n")
                fo.close()
                return True

            for col in range(i + 1, n):
                if int(board_copy[row][col]) == 2:
                    if DFS(row, col + 1, cnt, board_copy):
                        return True

            if row < n - 1:
                if DFS(row + 1, 0, cnt, board_copy):
                    return True

            if row == n - 1 and i == n - 1:
                return False

    if flg == 0 and row < n - 1:
        if DFS(row + 1, 0, cnt, board_copy):
            return True

#------------------------------------------------------------------------#
#------------------------------------------------------------------------#


def BFS(board):
    #print("IN BFS")
    global board_size
    global no_of_lizards
    n = board_size
    l = no_of_lizards
    q = queue.Queue()
    board_copy = [k[:] for k in board]
    a = []
    a.append(0)
    a.append(0)
    a.append(0)
    a.append(board_copy)
    q.put(a)
    while q.empty() is False:
        b = q.get()
        flg = 0
        for clm in range(b[1],n):
            board_copy = [k[:] for k in b[3]]
            if safe_to_place(board_copy,b[0],clm):
                flg = 1
                board_copy[b[0]][clm] = '1'
                cnt = b[2] + 1

                if cnt == l:
                    fo = open("output.txt", 'w')
                    fo.write("OK\n")
                    for a in board_copy:
                        fo.write("".join(map(str, a)) + "\n")
                    fo.close()
                    return True

                for col in range(clm + 1, n):
                    if int(board_copy[b[0]][col]) == 2:
                        a = []
                        a.append(b[0])
                        a.append(col+1)
                        a.append(cnt)
                        a.append(board_copy)
                        q.put(a)

                if b[0] < n - 1:
                    a = []
                    a.append(b[0]+1)
                    a.append(0)
                    a.append(cnt)
                    a.append(board_copy)
                    q.put(a)

        if flg == 0 and b[0] < n-1:
            a = []
            a.append(b[0] + 1)
            a.append(0)
            a.append(b[2])
            a.append(b[3])
            q.put(a)

    return False


#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#


def safe_to_place(board, row, clm):
    global board_size
    global no_of_lizards
    n = board_size
    l = no_of_lizards
    if board[row][clm] == '1' or board[row][clm] == '2':
        return False
    row_before = check_row_before(board,n,row,clm)
    if row_before is False:
        return False

    column_above = check_col_above(board,n,row,clm)
    if column_above is False:
        return False

    left_diagonal = check_left_diagonal(board,n,row,clm)
    if left_diagonal is False:
        return False

    right_diagonal = check_right_diagonal(board, n, row, clm)
    if right_diagonal is False:
        return False

    return True


def check_row_before(board,n,row,clm):
    if clm != 0:
        for j in range (clm-1,-1,-1):
            if (board[row][j] == '2'):
                return True
            elif (board[row][j] == '1') :
                return False
            else:
                continue
        return True
    else:
        return True


def check_col_above(board, n , row,clm):
    if row != 0:
        for j in range (row-1,-1,-1):
            if (board[j][clm] == '2'):
                return True
            elif (board[j][clm] == '1') :
                return False
            else:
                continue
        return True
    else:
        return True


def check_left_diagonal(board,n,row,clm):
    i = row - 1
    j = clm - 1
    while i >= 0 and j >=0:
        if board[i][j] == '2':
            return True
        elif board[i][j] == '1':
            return False
        else:
            i = i-1
            j = j-1
            continue
    return True


def check_right_diagonal(board,n,row,clm):
    i = row - 1
    j = clm + 1
    while i >= 0 and j < n:
        if board[i][j] == '2':
            return True
        elif board[i][j] == '1':
            return False
        else:
            i = i-1
            j = j+1
            continue
    return True

#------------------------------------------------------------------------#
#------------------------------------------------------------------------#


def SA(n, l, board):
    #print("IN SA\n")
    startTime = datetime.datetime.now()
    temperature = 35
    alpha = 0.2
    iterations = 5
    curr_board = generate_random(n, l, board)
    curr_attacks = check_attacks(curr_board, n)
    while temperature > 0:
        while iterations > 0 and curr_attacks > 0:
            temp_board = generate_next_random_state(curr_board,n,l)
            new_attacks = check_attacks(temp_board,n)
            delta = new_attacks - curr_attacks
            val = probability_fun(delta, temperature)
            if (delta <= 0) or (val is True):
                curr_board = [k[:] for k in temp_board]
                curr_attacks = new_attacks
            endTime = datetime.datetime.now()
            elapsedTime = (endTime - startTime).total_seconds()
            #print (elapsedTime)
            if elapsedTime >= 290:
                return False
        if curr_attacks == 0:
            #print(curr_board)
            fo = open("output.txt", 'w')
            fo.write("OK\n")
            for a in curr_board:
                fo.write("".join(map(str, a)) + "\n")
            fo.close()
            return True

        iterations *=10
        temperature *= 1 - alpha
    return False


def probability_fun(delta, temperature):
    energy = -delta / temperature
    try:
        exp_energy = math.exp(energy)
    except OverflowError:
        return False
    rand_num = random.uniform(0, 1)
    if exp_energy > rand_num:
        return True
    else:
        return False


def generate_random(n,l,board):
    for i in range(0,l):
        while True:
            x = random.randint(0,n-1)
            y = random.randint(0,n-1)
            if board[x][y] == '0':
                board[x][y] = '1'
                break
    return board


def generate_next_random_state(board,n,l):
    dict = {}
    num = 0
    for i in range(0,n):
        for j in range(0,n):
            if board[i][j] == '1':
                dict[num] = [i, j]
                num = num + 1
    queen = random.randint(0,l-1)
    qx, qy = dict[queen]
    while True:
        row_rand = random.randint(0, n - 1)
        col_rand = random.randint(0, n - 1)
        if ((row_rand != qx or col_rand != qy) and board[row_rand][col_rand] == '0'):
            board[qx][qy] = '0'
            board[row_rand][col_rand] = '1'
            return board

#------------------------------------------------------------------------#
#------------------------------------------------------------------------#


def check_attacks(board,n):
    cnt = 0
    for row in range(0, n):
        for clm in range(0, n):
            if board[row][clm] == '1':
                for j in range(clm + 1, n):
                    if (board[row][j] == '2'):
                        break
                    elif (board[row][j] == '1'):
                        cnt = cnt + 1
                        break
                for j in range(row + 1, n):
                    if (board[j][clm] == '2'):
                        break
                    elif (board[j][clm] == '1'):
                        cnt = cnt + 1
                        break

                i = row + 1
                j = clm + 1
                while i <= n - 1 and j <= n - 1:
                    if board[i][j] == '2':
                        break
                    elif board[i][j] == '1':
                        cnt = cnt + 1
                        break
                    else:
                        i = i + 1
                        j = j + 1

                i = row + 1
                j = clm - 1
                while i <= n - 1 and j >= 0:
                    if board[i][j] == '2':
                        break
                    elif board[i][j] == '1':
                        cnt = cnt + 1
                        break
                    else:
                        i = i + 1
                        j = j - 1
    return cnt

#--------------------------------------------------------------------#
#--------------------------------------------------------------------#


def main():
    getBoard()


if __name__ == '__main__':
    main()
