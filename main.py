# main.py
import os
import sys

# Ensure project root in path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from smart_courier.utils import load_packages_csv, load_vans_csv, load_edge_list_csv
from smart_courier.assignment import assign_packages_greedy, assign_packages_knapsack
from smart_courier.routing import build_graph, dijkstra


DEPOT = "A"


def print_van_routes(assignments, graph, strategy_name):
    print(f"\n{strategy_name} – Van Routes")
    print("----------------------------------")
    for van_id, pkgs in assignments.items():
        if not pkgs:
            continue
        destinations = {p.destination for p in pkgs}
        print(f"Van {van_id} delivers {len(pkgs)} packages:")
        for dest in destinations:
            path, dist = dijkstra(graph, DEPOT, dest)
            print(f"   → Destination {dest}: Path {path} (Distance {dist})")
        print()
    print("----------------------------------\n")


def compare_strategies(order_count, min_priority, vans_to_use, packages, vans, graph):
    eligible_packages = [p for p in packages if p.priority >= min_priority]
    total_before = len(packages)
    total_after = len(eligible_packages)

    selected_packages = sorted(
        eligible_packages, key=lambda p: p.priority, reverse=True
    )[:order_count]

    active_vans = vans[:vans_to_use]

    # Greedy
    greedy_assignments = assign_packages_greedy(selected_packages, active_vans)
    greedy_delivered = sum(len(pkgs) for pkgs in greedy_assignments.values())
    greedy_leftover = len(selected_packages) - greedy_delivered
    greedy_vans_used = sum(1 for pkgs in greedy_assignments.values() if pkgs)
    greedy_idle = vans_to_use - greedy_vans_used

    # Knapsack
    knapsack_assignments = assign_packages_knapsack(selected_packages, active_vans)
    knapsack_delivered = sum(len(pkgs) for pkgs in knapsack_assignments.values())
    knapsack_leftover = len(selected_packages) - knapsack_delivered
    knapsack_vans_used = sum(1 for pkgs in knapsack_assignments.values() if pkgs)
    knapsack_idle = vans_to_use - knapsack_vans_used

    print(f"\nComparing strategies for {order_count} packages (priority ≥ {min_priority})...")
    print(f"Total packages available: {total_before}")
    print(f"Eligible after priority filter: {total_after}")
    print(f"Vans available: {len(vans)}, Vans chosen: {vans_to_use}")
    print("-------------------------------------------------------")
    print("Greedy Assignment")
    print(f"   Vans used: {greedy_vans_used} / {vans_to_use}")
    print(f"   Packages delivered: {greedy_delivered}")
    print(f"   Leftover: {greedy_leftover}")
    print(f"   Idle vans: {greedy_idle}\n")

    print("Knapsack Assignment")
    print(f"   Vans used: {knapsack_vans_used} / {vans_to_use}")
    print(f"   Packages delivered: {knapsack_delivered}")
    print(f"   Leftover: {knapsack_leftover}")
    print(f"   Idle vans: {knapsack_idle}\n")

    if knapsack_delivered > greedy_delivered:
        print(f"Winner: Knapsack (+{knapsack_delivered - greedy_delivered} more delivered)")
    elif greedy_delivered > knapsack_delivered:
        print(f"Winner: Greedy (+{greedy_delivered - knapsack_delivered} more delivered)")
    else:
        print("Result: Tie (both delivered the same number of packages)")
    print("-------------------------------------------------------\n")

    print_van_routes(greedy_assignments, graph, "Greedy")
    print_van_routes(knapsack_assignments, graph, "Knapsack")


def main():
    packages = load_packages_csv("data/packages.csv")
    vans = load_vans_csv("data/vans.csv")
    edge_list = load_edge_list_csv("data/edges.csv")
    graph = build_graph(edge_list)

    while True:
        user_input = input("How many packages to deliver? (or 'exit'): ").strip()
        if user_input.lower() == "exit":
            print("Exiting Smart Courier. Goodbye!")
            break
        if not user_input.isdigit():
            print("Please enter a valid number.\n")
            continue
        order_count = int(user_input)

        pr_input = input("Enter minimum priority (1–5): ").strip()
        min_priority = int(pr_input) if pr_input.isdigit() else 1

        van_input = input(f"How many vans to use? (max {len(vans)}): ").strip()
        vans_to_use = min(int(van_input), len(vans)) if van_input.isdigit() else len(vans)

        if order_count <= 0:
            print("Please enter a number greater than 0.\n")
            continue

        compare_strategies(order_count, min_priority, vans_to_use, packages, vans, graph)


if __name__ == "__main__":
    main()
