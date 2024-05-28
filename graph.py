#!/usr/bin/python3

class Graph:
    def __init__(self, vertices, edges, directed=False):
        self.vertices = vertices
        self.edges = edges
        self.directed = directed
        self.graph = {vertex: [] for vertex in vertices}
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            if not directed:
                self.graph[edge[1]].append(edge[0])

    def dfs(self):
        visited = {vertex: False for vertex in self.vertices}
        entry_exit = {}

        def dfs_visit(vertex, time):
            visited[vertex] = True
            entry_time = time[0]
            time[0] += 1
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    dfs_visit(neighbor, time)
            exit_time = time[0]
            time[0] += 1
            entry_exit[vertex] = (entry_time, exit_time)

        time = [1]
        for vertex in self.vertices:
            if not visited[vertex]:
                dfs_visit(vertex, time)

        return entry_exit

# Example usage
g = Graph(['a', 'b', 'c', 'd'], [('a', 'c'), ('d', 'a'), ('b', 'c'), ('b', 'd')], directed=True)
print(g.dfs())  # Should print the entry and exit times for each vertex
