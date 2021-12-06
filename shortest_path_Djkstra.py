import sys
from heapq import heapify, heappush, heappop

def dijsktra(graph, src, dest):
    inf = sys.maxsize                   # create infinite value.

    # create a dictionary of dictionaries
    node_data={
        'A':{'cost':inf,'pred':[]},     # it was starting node / source node --> we have to reassign it 0
        'B':{'cost':inf,'pred':[]},
        'C':{'cost':inf,'pred':[]},
        'D':{'cost':inf,'pred':[]},
        'E':{'cost':inf,'pred':[]},
        'F':{'cost':inf,'pred':[]},
        }
    node_data[src]['cost'] = 0          # reassign A
    visited=[]
    temp=src                            # here temp is actually the current node

    for i in range(5):              # (n-1) steps
        if temp not in visited:     # check temp is available in visited.
            visited.append(temp)
            min_heap=[]
            for j in graph[temp]:       # here graph is the hole dict, temp is A, B, C, D, E, F & 'j' is the inner value of them
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                            # cost of temp              cost of temp-->j(inner dict)
                    if cost < node_data[j]['cost']:     # compare the cost with the existing cost of node data
                        node_data[j]['cost'] = cost

                        # find out the path
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                    # calculate the cost
                    heappush(min_heap, (node_data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print('Shortest Distance: ' + str(node_data[dest]['cost']))
    print('Shortest Path: ' + str(node_data[dest]['pred'] + list(dest)))

if __name__ == "__main__":
    graph={
        'A':{'B':2, 'C':5, 'F':11},
        'B':{'A':2, 'C':8, 'D':5, 'E':13},
        'C':{'A':5, 'B':8, 'E':12},
        'D':{'B':5, 'E':1, 'F':17},
        'E':{'B':13, 'C':12, 'D':1},
        'F':{'A':11, 'D':17}
    }

    source = 'A'
    destination='F'
    dijsktra(graph, source, destination)


'''
'A':{'B':2, 'C':4},
'B':{'A':2, 'C':3, 'D':8},
'C':{'A':4, 'B':3, 'E':5, 'D':2},
'D':{'B':8, 'C':2, 'E':11, 'F':22},
'E':{'C':5, 'D':11, 'F':1},
'F':{'D':22, 'E':1}
'''

'''
'A':{'B':2, 'C':5, 'F':11},
'B':{'A':2, 'C':8, 'D':5, 'E':13},
'C':{'A':5, 'B':8, 'E':12},
'D':{'B':5, 'E':1, 'F':17},
'E':{'B':13, 'C':12, 'D':1},
'F':{'A':11, 'D':17}
'''