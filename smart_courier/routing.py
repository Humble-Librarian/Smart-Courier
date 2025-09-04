from typing import Dict, List, Tuple
from .graph import Graph
from .models import Van, Package

def route_for_van(graph: Graph, van: Van, packages: List[Package]) -> Tuple[List[str],float]:
    if not packages: return [van.start],0.0
    remaining=set(p.destination for p in packages)
    route=[van.start]; total=0.0; cur=van.start
    while remaining:
        dist,_=graph.dijkstra(cur)
        next_node=min(remaining,key=lambda n:dist[n])
        d=dist[next_node]
        total+=d; route.append(next_node)
        remaining.remove(next_node); cur=next_node
    return route,total

def compute_routes(graph: Graph, assignments: Dict[str,List[Package]], vans: List[Van]) -> Dict[str,Tuple[List[str],float]]:
    van_map={v.vid:v for v in vans}; out={}
    for vid,pkgs in assignments.items():
        out[vid]=route_for_van(graph,van_map[vid],pkgs)
    return out
