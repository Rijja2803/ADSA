import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue to explore the nodes with the smallest distance first
    pq = [(0, start)]  # (distance, vertex)

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip if the current distance is not the shortest found so far
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

start = 'A'
distances = dijkstra(graph, start)
print(distances)  # Output the shortest distances from the start vertex
