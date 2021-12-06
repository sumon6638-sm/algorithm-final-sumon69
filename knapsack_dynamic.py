# a dynamic approach
# Returns the maximum value that can be stored by the bag
def knapSack(W, wt, val, n):
   K = [[0 for x in range(W + 1)] for x in range(n + 1)]
   #Table in bottom up manner
   for i in range(n + 1):
      for j in range(W + 1):
         if i == 0 or j == 0:
            K[i][j] = 0
         elif wt[i-1] <= j:
            K[i][j] = max(val[i-1] + K[i-1][j-wt[i-1]], K[i-1][j])
         else:
            K[i][j] = K[i-1][j]
   return K[n][W]
#Main
val = [4, 3, 6, 5]
wt = [3, 2, 5, 4]
W = 5
n = len(val)
print(knapSack(W, wt, val, n))