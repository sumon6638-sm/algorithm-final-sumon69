#Returns the maximum value that can be stored by the bag
def knapSack(capacity, weight, profit, n):
   # initial conditions
   if n == 0 or capacity == 0 :
      return 0
   # If weight is higher than capacity then it is not included
   if (weight[n - 1] > capacity):
      return knapSack(capacity, weight, profit, n - 1)
   # return either nth item being included or not
   else:
      return max(profit[n - 1] + knapSack(capacity - weight[n - 1], weight, profit, n - 1),
                 knapSack(capacity, weight, profit, n - 1))




# To test above function
'''
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
'''

profit = [4, 3, 6, 5]
weight = [3, 2, 5, 4]
capacity = 5

n = len(profit)
print(knapSack(capacity, weight, profit, n))