
from .knapsack import knapsack_01

def assign_packages_knapsack(vans, packages):
    assignments={}; remaining=packages[:]
    for van in vans:
        _,chosen=knapsack_01(remaining,van.capacity)
        assignments[van.id]=chosen
        for p in chosen: remaining.remove(p)
    return assignments

def assign_packages_greedy(vans, packages):
    assignments={}; remaining=sorted(packages,key=lambda p:p.value/p.weight,reverse=True)
    for van in vans:
        cap=van.capacity; load=[]
        for p in remaining[:]:
            if p.weight<=cap:
                load.append(p); cap-=p.weight; remaining.remove(p)
        assignments[van.id]=load
    return assignments
