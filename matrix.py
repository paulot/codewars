def count_ways(n, m):
  dp = [[0 for i in range(0, n+1)] for j in range(0, m+1)]
  dp[1][1] = 1
  for i in range(1, n+1):
    for j in range(1, m+1):
      dp[i][j] += dp[i-1][j] + dp[i][j-1]
  return dp[n][m]

