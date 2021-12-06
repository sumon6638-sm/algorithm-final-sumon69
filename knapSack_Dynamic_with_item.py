
def knapSack(capacity, weight, profit, item):

    #Build Table K[][]
    K = [[0 for x in range(capacity + 1)]
         for x in range(item + 1)]

    # Build table K[][] in bottom
    # up manner
    for i in range(item + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif weight[i - 1] <= j:
                K[i][j] = max(profit[i - 1] + K[i - 1][j - weight[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    # stores the result of Knapsack
    maxProfit = K[item][capacity]
    print('Maximum profit: ', maxProfit)

    j = capacity
    for i in range(item, 0, -1):
        if maxProfit <= 0:
            break
        '''
         either the result comes from the
         top (K[i-1][j]) or from (profit[i-1]
         + K[i-1] [j-weight[i-1]]) as in Knapsack
         table. If it comes from the latter
         one/ it means the item is included.
        '''
        if maxProfit == K[i - 1][j]:
            continue
        else:
            # This item is included.
            print(weight[i - 1])

            # Since this weight is included
            # its profitue is deducted
            maxProfit = maxProfit - profit[i - 1]
            j = j - weight[i - 1]


s = int(input('Enter number of elements: '))

weight = []
print('Enter the value for weight')
for i in range(0, s):
   elements = int(input())
   weight.append(elements)
print('The array of weight look like: ', weight)

profit = []
print('Enter the value for profit')
for i in range(0, s):
   element = int(input())
   profit.append(element)
print('The array of profit look like: ', profit)

capacity = int(input('Enter the value of Capacity: '))

item = len(profit)

knapSack(capacity, weight, profit, item)



'''
profit = [4, 3, 6, 5]
weight = [3, 2, 5, 4]
capacity = 5
'''