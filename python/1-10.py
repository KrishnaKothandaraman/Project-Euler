

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

print(p10(2_000_000))