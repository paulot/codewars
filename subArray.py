"""
  Find the maximum sum of a contiguous array within a given array.
"""
def subsum(arr):
  if not arr:
    return None
  csum, msum = (0, arr[0])
  for num in arr:
    csum += num
    msum = max(csum, msum)
    if csum < 0:
      csum = 0

  return msum

