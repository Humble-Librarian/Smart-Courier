
import heapq
class Graph:
    def __init__(self): self.adj={}
    def add_edge(self,u,v,w):
        self.adj.setdefault(u,[]).append((v,w)); self.adj.setdefault(v,[]).append((u,w))
    def dijkstra(self,src):
        dist={n:float('inf') for n in self.adj}; dist[src]=0; pq=[(0,src)]
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist[u]: continue
            for v,w in self.adj[u]:
                if dist[v]>d+w:
                    dist[v]=d+w; heapq.heappush(pq,(dist[v],v))
        return dist
