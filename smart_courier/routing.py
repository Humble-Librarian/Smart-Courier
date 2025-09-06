# smart_courier/routing.py
import heapq

def build_graph(edge_list):
    """
    Build adjacency list graph from list of edges.
    edge_list: list of tuples (u, v, weight)
    """
    graph = {}
    for u, v, w in edge_list:
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))  # undirected
    return graph


def dijkstra(graph, source, target):
    """
    Dijkstra's shortest path algorithm.
    graph: adjacency list {node: [(neighbor, weight), ...]}
    source: start node
    target: destination node
    Returns: (path, distance)
    """
    queue = [(0, source, [])]
    seen = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        seen.add(node)

        if node == target:
            return (path, cost)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in seen:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return ([], float("inf"))
