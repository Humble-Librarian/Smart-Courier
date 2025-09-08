from smart_courier.knapsack import knapsack_assign

def assign_packages_greedy(packages, vans):
    # Assign packages using greedy approach (value-to-weight ratio)
    assignments = {van.id: [] for van in vans}
    
    # Sort packages by value per kg (highest first)
    for pkg in sorted(packages, key=lambda p: p.value/p.weight, reverse=True):
        # Try to fit package into first available van
        for van in vans:
            # Calculate current weight in van
            used = sum(p.weight for p in assignments[van.id])
            # Check if van has space for package
            if used + pkg.weight <= van.capacity:
                # Add package to van
                assignments[van.id].append(pkg)
                break
    return assignments

def assign_packages_knapsack(packages, vans):
    # Assign packages using knapsack optimization
    assignments = {van.id: [] for van in vans}
    remaining = packages[:]
    
    # Process each van
    for van in vans:
        # Use knapsack to find best packages for this van
        chosen = knapsack_assign(remaining, van.capacity)
        assignments[van.id] = chosen
        # Remove assigned packages from remaining list
        for pkg in chosen:
            remaining.remove(pkg)
    return assignments
