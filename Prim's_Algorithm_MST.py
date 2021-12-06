
INF = 9999999
# number of vertices in graph
V = 5

G = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
]

selected = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0

selected[0] = True
# print for edge and weight
print("Edge : Weight\n")
minimum_cost = 0
while (no_edge < V - 1):

    minimum = INF
    x = 0
    y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]

                        x = i
                        y = j

    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))

    for i in str(G[x][y]):
        minimum_cost = minimum_cost + int(G[x][y])
        print('Minimum Cost: ', minimum_cost)

    selected[y] = True
    no_edge += 1







'''
G = [
    [0, 9, 75, 0, 0],              # 0->0=0 || 0->1=9 || 0->2=75 || 0->3=0 || 0->4=0
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
    ]
'''