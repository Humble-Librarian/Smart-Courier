# This file implements the knapsack algorithm for optimal package selection

def knapsack_assign(packages, capacity):
    # Find best packages to maximize value within weight limit
    n = len(packages)
    
    # Create value table for dynamic programming
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    
    # Create decision table to track package selection
    keep = [[0]*(capacity+1) for _ in range(n+1)]
    
    # Fill tables using dynamic programming
    for i in range(1, n+1):
        w = packages[i-1].weight
        v = packages[i-1].value
        for c in range(1, capacity+1):
            # Check if package fits and improves value
            if w <= c and v + dp[i-1][c-w] > dp[i-1][c]:
                # Include package
                dp[i][c] = v + dp[i-1][c-w]
                keep[i][c] = 1
            else:
                # Skip package
                dp[i][c] = dp[i-1][c]
    
    # Reconstruct solution by backtracking
    res = []
    c = capacity
    for i in range(n, 0, -1):
        if keep[i][c] == 1:
            # Add selected package
            res.append(packages[i-1])
            c -= packages[i-1].weight
    
    return res
