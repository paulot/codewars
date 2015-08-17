from random import randint as r

# Find all pairs of words that form a palindromes

# to do this we can check if all prefixes of a word are in the set
# such that the sufix is a palindrome

def palPair(lis):
  lis = set(lis)
  ans = []
  for word in lis:
    for i in xrange(0, len(word)):
      prefix = word[:i]
      sufix = word[i:]
      print word, prefix, sufix
      if prefix[::-1] != word and sufix == sufix[::-1] and prefix[::-1] in lis:
        ans.append((word, prefix[::-1]))
      elif sufix[::-1] != word and prefix == prefix[::-1] and sufix[::-1] in lis:
        ans.append((sufix[::-1], word))
  return ans

def check(lis):
  return filter(lambda t: t[0] != t[1] and t[0]+t[1] == ((t[0]+t[1])[::-1]),
                [(w1,w2) for w2 in lis for w1 in lis])

chars = 'asdfghjklqwertyuiopzxcvbnm'

print palPair(['oo', 'c', 'ltp', 'mzvm', 'o'])
print check(['oo', 'c', 'ltp', 'mzvm', 'o'])
'''
for i in xrange(0, 10000):
  test = list(set(
    [''.join([chars[r(0, len(chars)-1)] for _ in xrange(0, r(1, 4))])
      for _ in xrange(0, r(1, 5))]))
  print "testing with", test
  #0# assert palPair(test) == check(test)
'''
