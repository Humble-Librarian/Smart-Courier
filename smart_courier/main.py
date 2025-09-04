from .utils import load_packages_csv, load_vans_csv, load_edge_list_csv
from .graph import Graph
from .assignment import assign_packages_greedy
from .routing import compute_routes
import os

def run_demo():
    base=os.path.join(os.getcwd(),'data')
    packages=load_packages_csv(os.path.join(base,'packages.csv'))
    vans=load_vans_csv(os.path.join(base,'vans.csv'))
    edges=load_edge_list_csv(os.path.join(base,'traffic_graph.csv'))
    g=Graph.from_edge_list(edges)
    assignments=assign_packages_greedy(packages,vans)
    routes=compute_routes(g,assignments,vans)
    print('\n=== Demo Output ===')
    for vid,(route,cost) in routes.items():
        print(f'{vid}: route={route} cost={cost}')

if __name__=='__main__': run_demo()
