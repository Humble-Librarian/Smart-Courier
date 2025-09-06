def knapsack_assign(packages, capacity):
    n = len(packages)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    keep = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        w = packages[i-1].weight
        v = packages[i-1].value
        for c in range(1, capacity+1):
            if w <= c and v + dp[i-1][c-w] > dp[i-1][c]:
                dp[i][c] = v + dp[i-1][c-w]
                keep[i][c] = 1
            else:
                dp[i][c] = dp[i-1][c]
    res = []
    c = capacity
    for i in range(n,0,-1):
        if keep[i][c] == 1:
            res.append(packages[i-1])
            c -= packages[i-1].weight
    return res
