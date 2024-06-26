import math

def p11():
    grid =  """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
            49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
            81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
            52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
            22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
            24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
            32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
            67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
            24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
            21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
            78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
            16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
            86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
            19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
            04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
            88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
            04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
            20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
            20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
            01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
    grid = [[int(num) for num in line.strip().split(" ")] for line in grid.split("\n")]
    ans = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                continue
            
            rightFour = 1
            downFour = 1
            diag = 1
            r_diag = 1
            if col + 3 < len(grid[0]):
                for i in range(4):
                    rightFour *= grid[row][col+i]
            if row + 3 < len(grid):
                for i in range(4):
                    downFour *= grid[row+i][col]
            if row + 3 < len(grid) and col + 3 < len(grid[0]):
                for i in range(4):
                    diag *= grid[row+i][col+i]
            if row + 3 < len(grid) and col - 3 >= 0:
                for i in range(4):
                    r_diag *= grid[row+i][col-i]
        
            ans = max(ans, downFour, rightFour, diag, r_diag)
    print(ans)

def p12():
    j = 8
    t = 28
    while j < 3_000_000:
        t += j
        upper = int(math.sqrt(t))
        n = t
        mp = {i:0 for i in range(upper+1)}
        while n % 2 == 0:
            n = n // 2
            mp[2] += 1
        for i in range(3,upper+1,2):
            if n == 1:
                break
            while n % i== 0:
               n = n // i
               mp[i] += 1
        if n > 2:
            mp[2] += 1
        div = 1
        for _,val in mp.items():
            if val == 0:
                continue
            div *= (val+1)
        if div > 500:
            print(t)
            break
        j += 1


def p13(t):
    str(sum([int(tt) for tt in t.split("\n")]))[:10]


def p14():
    n = 13
    ans = 0
    max_n = 0
    while n < 1_000_000:
        n2 = n
        ans2 = 0
        while n2 != 1:
            if n2 % 2:
                n2 = 3*n2+1
            else:
                n2 = n2//2
            ans2 += 1
        if ans2 > ans:
            max_n = n
            ans = ans2
        n += 1
    print(max_n)

def p15(r, c, r_dim, c_dim, memo):
    if r >= r_dim or c >= c_dim:
        return 0
    if (r,c) in memo:
        return memo[(r,c)]
    if r == r_dim - 1 and c == c_dim - 1:
        return 1
    ans = 0
    ans += p15(r+1, c, r_dim, c_dim, memo)
    ans += p15(r, c+1, r_dim, c_dim, memo)
    memo[(r,c)] = ans
    return ans
    


