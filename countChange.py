"""
  For this problem define a function that counts the number of ways that you can
  make change given an ammount and a set of coins.
"""
def count_change(ammount, coins):
  """
    Counts the number of ways to make change by building a table from the bottom
    up. The table contains the number of ways you made change for that particular
    amoount.
  """
  dp = [[0 for i in range(0,len(coins) + 1)] for j in range(0, ammount)]
  dp.insert(0,[1 for i in range(0, len(coins)+1)])

  for c_ammount in range(1, len(dp)):
    for i, coin in enumerate(coins):
      dp[c_ammount][i+1] = dp[c_ammount][i]
      dp[c_ammount][i+1] += dp[c_ammount - coin][i+1] if coin <= c_ammount else 0

  for i in range(0, len(dp)):
    print dp[i]

  return dp[-1][-1]

def count_change_perfect(ammount, coins):
  """
    Like the last solution, however this one simplifies the table to a one
    dimensional list. This is possble as we are essentially summing the values
    down the table, so we don't need to keep the extra entries.
  """
  dp = [1] + [0] * ammount
  for coin in coins:
    for i in range(coin, ammount+1):
      dp[i] += dp[i-coin]
  return dp[-1]
