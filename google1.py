"""
  Find the missing ranges of numbers in the range 0-99.
  missing(12) -> 0-11, 13-99
  missing(1,2) -> 0, 3-99
  missing(3,4,8) -> 0-2, 5-7, 9-99
"""

from operator import itemgetter
from itertools import groupby

def missing(*nums):
  """
  For this algorithm we first find the numbers that are missing in the given
  range. Then, we group the missing numbers as consecutive numbers. For each
  group of consecutive numbers we generate a string in the format presented
  above.
  """
  # Get the numbers not present in the given set, but present in 0-99
  missingNums = sorted(list(set(range(0,100))^set(nums)))
  ranges = []

  # Group the numbers by the difference between their index and themselves.
  # This works since consecutive numbers will have the same value of
  # index - themselves.
  for k, g in groupby(enumerate(missingNums), lambda (i,x):i-x):
    # g will be a group object of tuples (i, num). For each tuple in g, get the
    # second value of the given group, this is the number. Once we get all
    # second values, then we have a list of consecutive integers
    group = map(itemgetter(1), g)

    # From that list format it according to the problem statement
    ranges.append('%s-%s' % (group[0], group[-1]) if len(group) > 1
        else str(group[0]))

  return ','.join(ranges)
