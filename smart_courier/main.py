
from .utils import load_packages_csv, load_vans_csv, load_edge_list_csv
from .assignment import assign_packages_knapsack, assign_packages_greedy
from .graph import Graph
from .routing import compute_routes

def main():
    print("🚚 Smart Courier V1")
    packages=load_packages_csv("data/packages.csv")[:100]
    vans=load_vans_csv("data/vans.csv")[:10]
    edges=load_edge_list_csv("data/edges.csv")
    choice=input("Choose strategy (greedy/knapsack): ").strip().lower()
    assignments=assign_packages_greedy(vans,packages) if choice=="greedy" else assign_packages_knapsack(vans,packages)
    print("\n📦 Package Allocation:")
    for vid,pkgs in assignments.items(): print(f"Van {vid}: {len(pkgs)} packages")
    g=Graph(); [g.add_edge(u,v,w) for u,v,w in edges]
    routes=compute_routes(g,"A"); print("\n📍 Shortest Paths from depot A:")
    for dest,dist in routes.items(): print(f"A → {dest}: {dist}")

if __name__=="__main__": main()
