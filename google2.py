"""
  Write a function that takes 2 strings. It shoud output the
  first string re-ordered according to the order of characters
  in the second string.
"""

def sortOnStr(str1, str2):
  """
  For this problem, we can use the built-in sorted and change the key
  function to sort the characters based on their index of the second string.
  If the character is not found in the second string, give it the last place.
  """
  return ''.join(sorted(str1, key=lambda c: str2.index(c) if c in str2
      else len(str1)))
