
def rule110(n):
    table = {
        0 : 0,
        1 : 1,
        2 : 1,
        3 : 1,
        4 : 0,
        5 : 1,
        6 : 1,
        7 : 0
    }
    board = []
    for _ in range(2):
        board.append([0]*n)

    board[0][n-2] = 1
    cur_board = 0
    for _ in range(n): 
        for i in range(n):
            if board[cur_board][i] == 0:
                print(" ",end = "")
            else:
                print("*", end ="")
        print()

        for i in range(n):
            a = board[cur_board][i-1]
            b = board[cur_board][i]
            c = board[cur_board][(i+1) % (n)]
            triplet = (a << 2) | (b << 1) | (c << 0)
            board[1-cur_board][i] = table[triplet]
            #print(f"Setting board {1-cur_board} = {table[val]}")
        
        cur_board = 1 - cur_board


def p10(n):
    x = [(i, 1) for i in range(n+1)]
    s = 0
    for i in range(2, n+1):
        if i >= len(x):
            continue

        if x[i][1] == 0:
            continue
        s += x[i][0]

        for j in range(x[i][0]**2, n+1, x[i][0]):
            x[j] = (x[j][0], 0)
    return s