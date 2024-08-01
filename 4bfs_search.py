
# Este es literalmente el mismo codigo que hicimos para el ejercicio 5 (hicimos primero el ejercicio cinco)
graph = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '5'],
    '4': ['2', '5'],
    '5': ['2', '3', '4']
}


def bfs_shortest_path(graph, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end:
                    return new_path

            visited.add(node)

    return None


start = '1'
end = '4'
path = bfs_shortest_path(graph, start, end)

print(path)
