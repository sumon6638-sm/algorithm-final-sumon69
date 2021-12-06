cost = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

def knapsack(n, W, wm, vm):
  for i in range(1, n+1):
    for w in range(1, W+1):
      if(wm[i] > w):
        cost[i][w] = cost[i-1][w]
      else:
        if ((vm[i]+cost[i-1][w-wm[i]]) > cost[i-1][w]):
          cost[i][w] = vm[i] + cost[i-1][w-wm[i]]
        else:
          cost[i][w] = cost[i-1][w]
  return cost[n][W]

def items_in_optimal(n, W, wm):
  i = n
  j = W

  while (i > 0 and j > 0):
    if(cost[i][j] != cost[i-1][j]):
      print(i)
      j = j-wm[i]
      i = i-1
    else:
      i = i-1

if __name__ == '__main__':
  # element at index 0 is fake. matrix starting from 1.
  wm = [3, 2, 5, 4]
  vm = [4, 3, 6, 5]
  print(knapsack(4, 5, wm, vm))
  items_in_optimal(4, 5, wm)