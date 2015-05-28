"""
  http://www.codewars.com/kata/did-you-mean-dot-dot-dot
"""
import copy

def levDistance(str1, str2):
  prev_dp = range(0, len(str2) + 1)
  cur_dp = range(0, len(str2) + 1)

  for i, c1 in enumerate(str1):
    cur_dp[0] = i+1
    for j, c2 in enumerate(str2):
      cur_dp[j+1] = min(cur_dp[j], prev_dp[j+1], prev_dp[j]) + 1 if c1 != c2 \
          else prev_dp[j]
    prev_dp = copy.copy(cur_dp)

  return cur_dp[len(str2)]

def mostSimilar(word, arr):
  return reduce(
      lambda a,b: a if a[0] < levDistance(b,word) else (levDistance(b, word), b),
      arr,
      (levDistance(arr[0], word), arr[0]))[1]
