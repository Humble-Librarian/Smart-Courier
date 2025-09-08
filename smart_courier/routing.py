# This file handles graph building and shortest path finding for delivery routes

import heapq

def build_graph(edge_list):
    # Build graph from edge list (source, target, weight)
    graph = {}
    for u, v, w in edge_list:
        # Add edge in both directions (undirected graph)
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))
    return graph

def dijkstra(graph, source, target):
    # Find shortest path using Dijkstra's algorithm
    queue = [(0, source, [])]
    seen = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        seen.add(node)

        if node == target:
            # Found target, return path and distance
            return (path, cost)

        # Explore neighbors
        for neighbor, weight in graph.get(node, []):
            if neighbor not in seen:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    # No path found
    return ([], float("inf"))
