from typing import List, Tuple
from .models import Package

def knapsack_dp(packages: List[Package], capacity: int) -> Tuple[float,List[Package]]:
    n=len(packages); W=capacity
    dp=[[0.0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        p=packages[i-1]
        for w in range(W+1):
            dp[i][w]=dp[i-1][w]
            if p.weight<=w:
                val=p.value+dp[i-1][w-p.weight]
                if val>dp[i][w]: dp[i][w]=val
    res=[]; w=W
    for i in range(n,0,-1):
        if dp[i][w]!=dp[i-1][w]:
            res.append(packages[i-1]); w-=packages[i-1].weight
    res.reverse()
    return dp[n][W],res
