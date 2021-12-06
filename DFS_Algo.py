# DFS algorithm in Python


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set() # visited ee 1ta array nicchi
    visited.add(start)

    print(start)

    for next in graph[start] - visited:  # next hocche adjajence
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3']),
         '2': set(['0', '4']),
         '3': set(['4']),
         '4': set(['2', '3'])}

dfs(graph, '0')