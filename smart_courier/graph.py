import heapq, math
from typing import Dict, Tuple, List, Optional

class Graph:
    def __init__(self):
        self.adj: Dict[str, List[Tuple[str,float]]] = {}

    def add_edge(self, u: str, v: str, w: float, undirected: bool=True):
        self.adj.setdefault(u, []).append((v, w))
        if undirected:
            self.adj.setdefault(v, []).append((u, w))

    def dijkstra(self, src: str) -> Tuple[Dict[str,float], Dict[str,Optional[str]]]:
        dist = {n: math.inf for n in self.adj}
        parent = {n: None for n in self.adj}
        dist[src] = 0.0
        pq = [(0.0, src)]
        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]: continue
            for v,w in self.adj.get(u, []):
                nd = d+w
                if nd < dist[v]:
                    dist[v] = nd
                    parent[v] = u
                    heapq.heappush(pq,(nd,v))
        return dist,parent

    def shortest_path(self, src: str, dst: str):
        dist,parent = self.dijkstra(src)
        if dist[dst]==math.inf: return math.inf,[]
        path=[]; cur=dst
        while cur is not None:
            path.append(cur); cur=parent[cur]
        return dist[dst], path[::-1]

    @classmethod
    def from_edge_list(cls, edges):
        g=cls()
        for u,v,w in edges: g.add_edge(u,v,w)
        return g
