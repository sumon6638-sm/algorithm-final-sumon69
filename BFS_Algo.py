import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()            # prottek ta vertex k nicchi
        # queue te add korar jonno
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:    # visisted vertex a Addjacent gulo na thakle segula add korbo...
                visited.add(neighbour)      # Adjacent adding
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3], 3: [1, 2, 4], 4: [0, 1, 3, 5], 5: [4]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)

# graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
#{0: [1, 2, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3], 3: [1, 2, 4], 4: [0, 1, 3, 5], 5: [4]}