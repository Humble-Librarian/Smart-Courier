
from typing import List, Tuple
from .models import Package

def knapsack_01(packages: List[Package], capacity: int) -> Tuple[int, List[Package]]:
    n=len(packages)
    dp=[[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        wt,val=packages[i-1].weight,packages[i-1].value
        for w in range(capacity+1):
            if wt<=w: dp[i][w]=max(val+dp[i-1][w-wt],dp[i-1][w])
            else: dp[i][w]=dp[i-1][w]
    chosen=[]; w=capacity
    for i in range(n,0,-1):
        if dp[i][w]!=dp[i-1][w]:
            chosen.append(packages[i-1]); w-=packages[i-1].weight
    return dp[n][capacity], list(reversed(chosen))
