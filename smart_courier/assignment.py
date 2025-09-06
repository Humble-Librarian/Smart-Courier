from smart_courier.knapsack import knapsack_assign

def assign_packages_greedy(packages, vans):
    assignments = {van.id: [] for van in vans}
    for pkg in sorted(packages, key=lambda p: p.value/p.weight, reverse=True):
        for van in vans:
            used = sum(p.weight for p in assignments[van.id])
            if used + pkg.weight <= van.capacity:
                assignments[van.id].append(pkg)
                break
    return assignments

def assign_packages_knapsack(packages, vans):
    assignments = {van.id: [] for van in vans}
    remaining = packages[:]
    for van in vans:
        chosen = knapsack_assign(remaining, van.capacity)
        assignments[van.id] = chosen
        for pkg in chosen:
            remaining.remove(pkg)
    return assignments
