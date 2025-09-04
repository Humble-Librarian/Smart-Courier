from typing import List, Dict
from .models import Package, Van
from .knapsack import knapsack_dp

def assign_packages_greedy(packages: List[Package], vans: List[Van]) -> Dict[str,List[Package]]:
    packs_sorted=sorted(packages,key=lambda p:p.value/p.weight if p.weight>0 else 0,reverse=True)
    state={v.vid:{'cap':v.capacity,'items':[]} for v in vans}
    for p in packs_sorted:
        candidate=None; best_left=None
        for v in vans:
            if state[v.vid]['cap']>=p.weight:
                left=state[v.vid]['cap']-p.weight
                if candidate is None or left<best_left:
                    candidate=v.vid; best_left=left
        if candidate:
            state[candidate]['items'].append(p)
            state[candidate]['cap']-=p.weight
    return {vid:info['items'] for vid,info in state.items()}

def assign_packages_knapsack(packages: List[Package], van: Van):
    return knapsack_dp(packages, van.capacity)
