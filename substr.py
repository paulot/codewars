"""
  Find the size of the longest common subtraing.
"""
def substr(str1, str2):
  dp = [[0 for i in range(0, len(str2)+1)] for j in range(0, len(str1)+1)]
  cmax = 0
  for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
      dp[i][j] += dp[i-1][j-1] + 1 if str1[i-1] == str2[j-1] else 0
      cmax = max(cmax, dp[i][j])

  """
  for i in range(0, len(str1)+1):
    print dp[i]
  """
  return cmax
