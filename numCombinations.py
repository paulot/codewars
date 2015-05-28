"""
  Make a program to count the number of combinations that are
  possible up to a given number.
"""
def numCombinations(n):
  if n < 0:
    return 0
  dp = [1]+[0]*n
  for num in xrange(1,n+1):
    for i in xrange(num,n+1):
      dp[i] += dp[i-num]
  return dp[-1]

