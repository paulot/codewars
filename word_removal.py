from collections import Counter, defaultdict


def f(words):
  words = list(reversed(sorted(words)))
  dp = defaultdict(int)
  count = Counter(words)
  max_chain = 0

  def dfs(word):
    if word in dp:
      return dp[word]

    if len(word) <= 1:
      dp[word] = 1
      return 1

    ans = 1

    for i in xrange(0, len(word)):
      candidate = '%s%s' % (word[:i], word[i+1:])
      if count[candidate] > 0:
        count[candidate] += 1
        count[word] -= 1
        ans = max(ans, 1 + dfs(candidate))
        count[candidate] -= 1
        count[word] += 1

    dp[word] = ans
    return ans

  return reduce(max, [dfs(word) for word in words])


print f(['a', 'b', 'ba', 'bca', 'bda', 'bdca'])
print f(['abc', 'adc', 'ac', 'bc'])
print f(['abcr', 'adc', 'ac', 'bc'])
