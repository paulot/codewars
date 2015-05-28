"""
  Module that defines an AI that chooses a move for nim
"""

def chooseMove(heaps):
  nimSum = lambda h: reduce(lambda a,b: a^b, h)
  for pile in range(0, len(heaps)):
    for straws in range(1, nimSum(heaps) + 1):
      heaps[pile] -= straws
      if nimSum(heaps) == 0:
        return pile, straws
      heaps[pile] += straws
